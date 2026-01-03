from src.skill_extractor import extract_skills

resume_text = """
I am a software engineer skilled in Python, SQL, and Machine Learning.
I have used Flask and Git for backend development.
"""

skills = extract_skills(resume_text)

print("Extracted Skills:")
print(skills)
