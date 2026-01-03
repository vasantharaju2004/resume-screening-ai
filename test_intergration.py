from src.skill_extractor import extract_skills
from src.matcher import match_skills, skill_match_score, text_similarity, final_score

resume_text = "Python ML developer with Flask and SQL experience"
jd_text = "Looking for Python Machine Learning engineer with NLP skills"

resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

matched, missing = match_skills(resume_skills, jd_skills)
skill_score = skill_match_score(matched, jd_skills)
text_score = text_similarity(resume_text, jd_text)

final = final_score(skill_score, text_score)

print("Skill Score:", skill_score)
print("Text Score:", text_score)
print("Final AI Score:", final)
