# Streamlit app
import streamlit as st

from src.resume_parser import extract_text_from_pdf
from src.matcher import rank_resumes

# database connection
from src.database import(
    create_tables,
    insert_job,
    insert_candidate,
    insert_result,
    fetch_resumes_from_db
)

# -----------------SETUP -----------------------
st.set_page_config(page_title="Resume Screening AI", layout="wide")

st.title("🤖 Resume Screening AI")
st.write("Upload resumes and paste a job description to rank candidatesusing AI.")


# ------------------------UI components-------------

st.subheader("📄 Upload Resumes (PDF)")
uploaded_files = st.file_uploader(
    "Upload multiple resumes",
    type=["pdf"],
    accept_multiple_files=True
)

st.subheader("📝 Job Description")

jd_text = st.text_area("Paste the job description here", height=200)

# when refresh the page ,pdf should remain in page
load_old = st.checkbox("Load previously uploaded resumes")

#---------------ACTION --------------------
#Analyze button core logic
if st.button("🚀 Analyze Resumes", key="analyze_main"):
    # initial process.
    if not jd_text.strip():
        st.error("Please enter a job description.")
        st.stop()

    resume_texts = []
    candidate_ids = []

    # -------- LOAD OLD RESUMES --------
    if load_old:
        resume_texts = fetch_resumes_from_db()

        if not resume_texts:
            st.warning("No resumes found in database.")
            st.stop()

        job_id = insert_job(jd_text)

    # -------- LOAD NEW RESUMES --------
    else:
        if not uploaded_files:
            st.error("Please upload at least one resume PDF.")
            st.stop()

        job_id = insert_job(jd_text)

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            if text.strip():
                resume_texts.append(text)
                cid = insert_candidate(text)
                candidate_ids.append(cid)

    # -------- ANALYSIS --------
    with st.spinner("Analyzing resumes using AI..."):
        results = rank_resumes(resume_texts, jd_text)

        if not load_old:
            for r, cid in zip(results, candidate_ids):
                insert_result(
                    job_id,
                    cid,
                    r["final_score"],
                    r["skill_score"],
                    r["text_score"]
                )
    # -------- DISPLAY --------
    st.success("Analysis completed successfully!")
    st.subheader("📊 Candidate Ranking")

    for idx, r in enumerate(results, start=1):
        with st.expander(f"🏅 Rank {idx} — Candidate {r['candidate_id']}"):
            st.metric("Final AI Score (%)", r["final_score"])
            col1, col2 = st.columns(2)
            col1.metric("Skill Score (%)", r["skill_score"])
            col2.metric("Text Similarity (%)", r["text_score"])

            st.write("✅ Matched Skills:")
            st.write(", ".join(r["matched_skills"]) or "None")

            st.write("❌ Missing Skills:")
            st.write(", ".join(r["missing_skills"]) or "None")
    
    




# database connections to streamlit


# create_tables()

# job_id = insert_job(jd_text)


# resume_texts = []
# candidate_ids = []

# for file in uploaded_files:
#     text = extract_text_from_pdf(file)
#     if text.strip():
#         resume_texts.append(text)
#         cid = insert_candidate(text)
#         candidate_ids.append(cid)
# results = rank_resumes(resume_texts, jd_text)

# for r, cid in zip(results, candidate_ids):
#     insert_result(
#         job_id,
#         cid,
#         r["final_score"],
#         r["skill_score"],
#         r["text_score"]
#     )





# footer
st.markdown("---")
st.caption("Built by Vasanth | Resume Screening AI using NLP & Machine Learning")
