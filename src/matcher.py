from  sklearn.feature_extraction.text import TfidfVectorizer

from  sklearn.metrics.pairwise import cosine_similarity

from src.skill_extractor import extract_skills

def match_skills(resume_skills, jd_skills):
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = resume_set.intersection(jd_set)
    missing = jd_set - resume_set

    return list(matched) , list(missing)

def skill_match_score(matched_skills, jd_skills):
    if not jd_skills:
        return 0.0
    
    score = (len(matched_skills) / len(jd_skills)) *100
    return round(score, 2)

def text_similarity(resume_text, jd_text):
    documents = [resume_text, jd_text]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return round(similarity[0][0] * 100, 2)

def final_score(skill_score, text_score, w1=0.6, w2=0.4):
    return round((w1 * skill_score) + (w2 * text_score), 2)


def rank_resumes(resume_texts, jd_text):
    results = []

    #temporary debug code
    # print("===== RAW JD TEXT =====")
    # print(jd_text[:500])

    # print("===== RAW RESUME TEXT =====")
    # print(resume_texts[:500])



    for idx, resume_text in enumerate(resume_texts):
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)

        matched = sorted(set(resume_skills) & set(jd_skills))
        missing = sorted(set(jd_skills) - set(resume_skills))

        skill_score = skill_match_score(matched, jd_skills)
        text_score = text_similarity(resume_text, jd_text)

        final = final_score(skill_score , text_score)

        results.append({
            "candidate_id": idx+1,
            "skill_score": skill_score,
            "text_score": text_score,
            "final_score": final,
            "matched_skills": matched,
            "missing_skills": missing
        })

    return sorted(results, key=lambda x: x["final_score"], reverse=True)
