import os
from docx import Document
from PyPDF2 import PdfReader

# Function to extract information from resumes (PDF/DOCX)
def extract_info_from_resume(resume_path):
    # Placeholder data for demonstration
    resume_data = {
        "work_experience": "",
        "education": "",
        "skills": ""
    }
    
    if resume_path.endswith('.pdf'):
        # Extract information from a PDF file
        with open(resume_path, "rb") as file:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            # Process text to extract work experience, education, skills
            resume_data["work_experience"] = "Extracted work experience from PDF"
            resume_data["education"] = "Extracted education from PDF"
            resume_data["skills"] = "Extracted skills from PDF"
            
    elif resume_path.endswith('.docx'):
        # Extract information from a DOCX file
        doc = Document(resume_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text
        # Process text to extract work experience, education, skills
        resume_data["work_experience"] = "Extracted work experience from DOCX"
        resume_data["education"] = "Extracted education from DOCX"
        resume_data["skills"] = "Extracted skills from DOCX"
    
    return resume_data

# Function to score the resume (dummy scoring example)
def score_resume(resume_data):
    # Calculate score based on the resume data (dummy score here)
    score = 85.0  # A static score for now
    return score
