from src.matcher import text_similarity

resume_text = """
Python developer with experience in machine learning,
data analysis, and backend development using Flask.
"""

jd_text = """
Looking for a machine learning engineer skilled in Python,
data analysis, and REST API development.
"""

score = text_similarity(resume_text, jd_text)
print("Text Similarity %:", score)
