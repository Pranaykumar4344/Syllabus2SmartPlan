import re
import fitz  # PyMuPDF

def parse_syllabus(file_or_text):
    if isinstance(file_or_text, str):
        text = file_or_text
    elif hasattr(file_or_text, 'name') and file_or_text.name.endswith(".pdf"):
        doc = fitz.open(stream=file_or_text.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
    else:
        text = file_or_text.read().decode("utf-8")

    text = text.replace('\r', '').strip()

    # Match units like "Unit 1: Title"
    unit_pattern = re.compile(r"(Unit\s*\d+):\s*(.+?)\n", re.IGNORECASE)
    matches = list(unit_pattern.finditer(text))

    units = []
    for i, match in enumerate(matches):
        unit_name = match.group(1).strip()
        unit_title = match.group(2).strip()

        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[start:end].strip()

        raw_topics = re.split(r",\s*|\n", content)
        topics = [t.strip("-•\n ") for t in raw_topics if len(t.strip()) > 2]

        units.append({
            "unit": unit_name,
            "title": unit_title,
            "topics": topics
        })

    return units
