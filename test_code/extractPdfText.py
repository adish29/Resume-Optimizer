import PyPDF2
import re
import spacy

# nlp = spacy.load("en_core_web_lg")

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = pdf_reader.pages[0].extract_text()
    return text

def preprocess_text(text):
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    return text

def extract_keywords(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return keywords

def use_jd(jd_path):
    with open(jd_path, 'r') as file:
        jd = file.read()
    return jd

def remove_blank_lines(text):
    lines = text.splitlines()
    non_blank_lines = [line.strip() for line in lines if line.strip()]
    result_text = '\n'.join(non_blank_lines)
    return result_text


pdf_path = "resume_samples\Adish_Devendra_Pathare_latest.pdf"
jd_path = "job_descriptions\jd1.txt"

resume_text = remove_blank_lines(preprocess_text(extract_text_from_pdf(pdf_path)))
# print(resume_text)
# print("------------------------------")
jd_text = remove_blank_lines(preprocess_text(use_jd(jd_path)))
# print(jd_text)

# keywords_jd = extract_keywords(jd_text)
# print("-----------------------------------------------")
# print(keywords_jd)


# r_t = nlp(resume_text)
# j_t = nlp(jd_text)
# print(r_t.similarity(j_t))
