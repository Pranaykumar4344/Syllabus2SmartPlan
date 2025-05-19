import pandas as pd
import os

def save_schedule(df):
    path = "data/schedules/study_schedule.csv"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    return path

def load_sample_text():
    with open("assets/sample_syllabus.txt", "r") as f:
        return f.read()
