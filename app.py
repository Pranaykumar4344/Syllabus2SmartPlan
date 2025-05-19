import streamlit as st
from PIL import Image
import pytesseract
from syllabus_parser import parse_syllabus
from scheduler import generate_schedule
from utils import save_schedule, load_sample_text
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.set_page_config(page_title="Syllabus2SmartPlan", layout="centered")
st.title("📚 Syllabus2SmartPlan")
st.markdown("Generate a custom study schedule from your syllabus.")

uploaded_file = st.file_uploader(
    "Upload your syllabus (.txt, .pdf) or photo (.jpg, .png)", 
    type=["txt", "pdf", "jpg", "jpeg", "png"]
)

syllabus_text = ""

# Load sample syllabus option
if not uploaded_file:
    with st.expander("📎 Or use sample syllabus"):
        sample_text = load_sample_text()
        st.code(sample_text)
        use_sample = st.button("Use Sample Syllabus")
        if use_sample:
            syllabus_text = sample_text

# Process uploaded file
if uploaded_file:
    file_type = uploaded_file.type

    if file_type.startswith("image/"):
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image Preview", use_column_width=True)
        with st.spinner("Extracting text from image..."):
            syllabus_text = pytesseract.image_to_string(image)
        st.text_area("Extracted text from image:", syllabus_text, height=250)

    elif file_type == "text/plain":
        syllabus_text = uploaded_file.getvalue().decode("utf-8")
        st.text_area("Syllabus Text:", syllabus_text, height=250)

    elif file_type == "application/pdf":
        st.warning("PDF parsing is not supported yet. Please upload text or image files.")
    else:
        st.error("Unsupported file type.")

if syllabus_text:
    topics = parse_syllabus(syllabus_text)
    if topics:
        st.success(f"Extracted {len(topics)} topics from syllabus.")

        # Set priority for each topic (optional)
        st.markdown("### Set priority for each topic (higher = more important)")
        priorities = []
        for i, topic in enumerate(topics):
            label = topic.get('title', str(topic)) if isinstance(topic, dict) else str(topic)
            priority = st.slider(f"Priority for: {label}", 1, 5, 3, key=f"priority_{i}")
            priorities.append((topic, priority))

        # Sort topics by priority descending
        sorted_topics = [t for t, p in sorted(priorities, key=lambda x: x[1], reverse=True)]

        st.markdown("### Enter Exam Date and Unavailable Dates")
        start_date = st.date_input("Exam Date (start date of study plan)", value=datetime.today())
        unavailable_dates_input = st.text_area(
            "Enter dates you are unavailable to study (comma separated, YYYY-MM-DD)", 
            placeholder="2025-05-20,2025-05-21"
        )

        unavailable_dates = []
        if unavailable_dates_input.strip():
            try:
                unavailable_dates = [
                    datetime.strptime(d.strip(), "%Y-%m-%d").date()
                    for d in unavailable_dates_input.split(",") if d.strip()
                ]
            except Exception as e:
                st.error(f"Invalid date format in unavailable dates: {e}")

        total_days = st.slider("📅 Number of days to prepare", 5, 120, 30)
        daily_hours = st.slider("⏰ Number of subtopics per day", 1, 10, 3)

        if st.button("Generate Study Plan"):
            with st.spinner("Generating study plan..."):
                df = generate_schedule(sorted_topics, total_days, daily_hours, start_date, unavailable_dates)

            # Show schedule as nicely formatted dates + subtopics
            for idx, row in df.iterrows():
                st.markdown(f"### {row['Date']}")
                st.markdown(row['Topics'].replace(", ", "\n\n"))  # Show each subtopic on separate lines with spacing

            path = save_schedule(df)
            with open(path, "rb") as f:
                st.download_button("Download Plan as CSV", f, file_name="study_schedule.csv")
    else:
        st.error("No topics extracted from the syllabus text.")
