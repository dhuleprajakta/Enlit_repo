# Main controller script
from resume_processor import extract_info_from_resume
from scoring import score_resume
from email_sender import send_email
import os

RESUME_DIR = "resumes"
LOG_FILE = "logs/processed.txt"

# Load already processed resumes
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'r') as f:
        processed = set(f.read().splitlines())
else:
    processed = set()

for file in os.listdir(RESUME_DIR):
    if file not in processed:
        resume_path = os.path.join(RESUME_DIR, file)
        name, email, text = extract_info_from_resume(resume_path)
        score, strengths, weaknesses = score_resume(text)
        send_email(name, email, score, strengths, weaknesses)

        with open(LOG_FILE, 'a') as f:
            f.write(file + '\n')

print("All resumes processed.")