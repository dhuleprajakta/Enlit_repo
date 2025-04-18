# Resume scoring logic
import re

def score_resume(text):
    score = 0
    strengths = []
    weaknesses = []

    if "machine learning" in text.lower():
        score += 20
        strengths.append("Has Machine Learning experience")
    else:
        weaknesses.append("Missing Machine Learning skills")

    if re.search(r'\bpython\b', text, re.IGNORECASE):
        score += 20
        strengths.append("Knows Python")
    else:
        weaknesses.append("No mention of Python")

    if "project" in text.lower():
        score += 20
        strengths.append("Has done projects")
    else:
        weaknesses.append("No project mentioned")

    if "intern" in text.lower():
        score += 20
        strengths.append("Has internship experience")
    else:
        weaknesses.append("No internship experience")

    if len(text.split()) > 250:
        score += 20
        strengths.append("Good resume length")
    else:
        weaknesses.append("Resume too short")

    return score, strengths, weaknesses

