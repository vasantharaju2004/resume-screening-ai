from src.resume_parser import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.matcher import match_skills, skill_match_score

with open("data/resumes/sample.pdf", "rb") as f:
    resume_text = extract_text_from_pdf(f)

jd_text = open("data/job_descriptions/sample_jd.txt").read()

resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

matched, missing = match_skills(resume_skills, jd_skills)
score = skill_match_score(matched, jd_skills)

print(matched, missing, score)
