
# 📚 Syllabus2SmartPlan

An intelligent and user-friendly study planner app built with **Streamlit** that converts your syllabus into a custom, trackable study schedule.

✨ Extract text from images, prioritize topics, avoid holidays, and download your schedule – all in a sleek interface!

**Live Demo**: [Syllabus2SmartPlan](https://syllabus2smartplan.streamlit.app)

---

## 🌟 Features

- 📂 Upload your syllabus as `.txt`, `.jpg`, `.jpeg`, or `.png`
- 🔍 OCR-powered image-to-text conversion using Tesseract
- 🧠 Intelligent topic extraction from unstructured syllabus text
- ⚡ Drag-and-drop priority setting for effective study
- 📅 Automatically generate plans avoiding your unavailable dates
- 📥 Download schedule as CSV directly from the app
- 💡 Use built-in sample syllabus for quick demos

---

## 🧠 How It Works

1. Upload your syllabus (text or image) or use a sample.
2. The app extracts topics and allows you to set priorities.
3. You select exam date and unavailable study days.
4. The app uses a scheduling algorithm to divide topics evenly.
5. You get a downloadable CSV study plan with daily tasks.

---

## 🛠️ Tech Stack

- Python 3.x
- Streamlit
- Pandas
- PIL (Pillow)
- pytesseract (OCR)
- Custom scheduling logic

---

## 📂 Project Structure

```
syllabus2smartplan/
│
├── app.py                  # Main Streamlit app
├── scheduler.py            # Scheduling engine
├── syllabus_parser.py      # Syllabus parsing logic
├── utils.py                # Utility functions
├── sample_syllabus.txt     # Example syllabus input
├── requirements.txt        # Project dependencies
└── README.md               # You're reading it!
```

---

## ⚙️ Installation (Local)

Clone the repository:

```
git clone https://github.com/Pranaykumar4344/syllabus2smartplan.git
cd syllabus2smartplan
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the app:

```
streamlit run app.py
```

---

## 🌐 Deployment on Streamlit Cloud

1. Push your project to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Choose `app.py` as the main file
5. Done! Your smart planner is live.

---

## 📊 Sample Input

- `sample_syllabus.txt` is available in the repo for quick testing.

---

## 🙋‍♂️ Author

**J Pranay Kumar**  
📧 JPranaykumar1205@gmail.com  
💼 [LinkedIn](https://www.linkedin.com/in/pranay-kumar-894651264)

---

## ⭐️ Show Your Support

If this project helped you:

- 🌟 Give it a star on GitHub
- 📣 Share it with friends or classmates
- ✏️ Fork it and build your own version!
