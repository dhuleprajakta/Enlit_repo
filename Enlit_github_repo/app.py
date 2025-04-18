import streamlit as st
import os
from resume_processor import extract_info_from_resume, score_resume

# Streamlit UI for file upload
st.title("AI Resume Scoring Tool")
uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_resume", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract information from the uploaded resume (pass only the file path)
    resume_data = extract_info_from_resume("temp_resume")

    # Score the resume based on extracted data
    score = score_resume(resume_data)

    # Display extracted information and the score
    st.write("Extracted Information:")
    st.json(resume_data)
    st.write(f"Resume Score: {score}")

    # Clean up the temporary file
    os.remove("temp_resume")
