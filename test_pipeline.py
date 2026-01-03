from src.resume_parser import extract_text_from_pdf
from src.text_cleaner import clean_text

if __name__ == "__main__":
    with open("data/resumes/sample.pdf", "rb") as f:
        raw_text = extract_text_from_pdf(f)

    print("----- RAW TEXT (first 500 chars) -----")
    print(raw_text[:500])

    cleaned_text = clean_text(raw_text)

    print("\n----- CLEANED TEXT -----")
    print(cleaned_text)
