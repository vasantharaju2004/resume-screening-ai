from src.matcher import rank_resumes

resumes = [
    "Python ML developer with SQL and Flask experience",
    "Java backend engineer with Spring and Docker",
    "Data scientist skilled in Python, Machine Learning, NLP"
]

jd_text = "Looking for Python Machine Learning engineer with NLP skills"

results = rank_resumes(resumes, jd_text)

for r in results:
    print(r)
