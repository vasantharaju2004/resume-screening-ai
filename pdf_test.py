import PyPDF2

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


# ---- TESTING WITH ONE PDF ----
if __name__ == "__main__":
    pdf_path = "test_resume.pdf"

    with open(pdf_path, "rb") as file:
        extracted_text = extract_text_from_pdf(file)

    print("------ EXTRACTED TEXT ------")
    print(extracted_text)
