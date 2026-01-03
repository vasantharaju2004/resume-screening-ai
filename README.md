# project documentation

# 🤖 Resume Screening AI

An AI-powered Resume Screening system that simulates an Applicant
Tracking System (ATS) using NLP and Machine Learning.

## 🚀 Features
- Resume parsing (PDF)
- Skill extraction using a curated skill taxonomy
- Resume ↔ Job Description matching
- TF-IDF + Cosine Similarity scoring
- Candidate ranking system
- SQLite database for persistence
- Streamlit web application

## 🧠 Tech Stack
- Python
- NLP (TF-IDF)
- Scikit-learn
- Streamlit
- SQLite

## 🏗️ Architecture
Upload Resume → Text Extraction → Skill Matching → AI Scoring → Ranking → UI

## ▶️ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
