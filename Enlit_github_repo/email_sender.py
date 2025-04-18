# Email sending script
import smtplib
from email.mime.text import MIMEText

def send_email(name, to_email, score, strengths, weaknesses):
    body = f"""
    Hi {name},

    Thank you for submitting your resume.

    Your CV Score: {score}/100

    Strengths:
    - " + "\n    - ".join(strengths) + "\n
    Areas to Improve:
    - " + "\n    - ".join(weaknesses) + "\n
    Best of luck!
    """

    msg = MIMEText(body)
    msg['Subject'] = "Your Resume Evaluation Report"
    msg['From'] = "your_email@example.com"
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.send_message(msg)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
