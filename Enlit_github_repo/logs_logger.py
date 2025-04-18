def log_processed_resume(resume_name):
    with open('logs/processed.txt', 'a') as f:
        f.write(resume_name + '\n')
