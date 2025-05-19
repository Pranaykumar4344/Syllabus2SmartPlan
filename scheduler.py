import pandas as pd
from datetime import timedelta

def flatten_topics(topics):
    flat_list = []
    for topic in topics:
        unit = topic.get('unit', '')
        title = topic.get('title', '')
        subtopics = topic.get('topics', [])
        for sub in subtopics:
            flat_list.append({"unit": unit, "title": title, "subtopic": sub})
    return flat_list

def format_subtopic(item):
    return f"{item['unit']}: {item['title']}\n   - {item['subtopic']}"

def generate_schedule(topics, total_days, daily_hours, start_date, unavailable_dates):
    flat_subtopics = flatten_topics(topics)

    total_slots = total_days * daily_hours
    # Here, one subtopic per slot (study hour)
    subtopics_per_slot = 1

    schedule = []
    current_index = 0
    current_date = start_date
    used_days = 0

    while current_index < len(flat_subtopics) and used_days < total_days:
        if current_date in unavailable_dates:
            current_date += timedelta(days=1)
            continue

        # For daily_hours > 1, assign multiple subtopics per day, otherwise one per day
        daily_subtopics = flat_subtopics[current_index: current_index + daily_hours]

        # Format each subtopic nicely
        daily_text = "\n\n".join(format_subtopic(sub) for sub in daily_subtopics)

        schedule.append({
            "Date": current_date.strftime("%Y-%m-%d"),
            "Topics": daily_text
        })

        current_index += daily_hours
        current_date += timedelta(days=1)
        used_days += 1

    return pd.DataFrame(schedule)
