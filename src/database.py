import sqlite3

DB_NAME = "resume_ai.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        job_id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS candidates (
        candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
        resume_text TEXT,
        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS results (
        result_id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER,
        candidate_id INTEGER,
        final_score REAL,
        skill_score REAL,
        text_score REAL
    )
    """)

    conn.commit()
    conn.close()

def insert_job(job_description):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO jobs (job_description) VALUES (?)",
        (job_description,)
    )
    conn.commit()
    job_id = cur.lastrowid
    conn.close()
    return job_id

def insert_candidate(resume_text):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO candidates (resume_text) VALUES (?)",
        (resume_text,)
    )
    conn.commit()
    candidate_id = cur.lastrowid
    conn.close()
    return candidate_id

def insert_result(job_id, candidate_id, final_score, skill_score, text_score):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO results (job_id, candidate_id, final_score, skill_score, text_score)
        VALUES (?, ?, ?, ?, ?)
    """, (job_id, candidate_id, final_score, skill_score, text_score))
    conn.commit()
    conn.close()


# for fetching resumes from the database in page
def fetch_resumes_from_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT resume_text FROM candidates")
    rows = cur.fetchall()

    conn.close()

    # Convert [(text1,), (text2,), ...] → [text1, text2, ...]
    return [row[0] for row in rows]
