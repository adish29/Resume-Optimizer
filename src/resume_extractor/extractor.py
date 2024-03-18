import re

from PyPDF2 import PdfReader
import spacy


class ResumeExtractor:
    def __init__(self, pdf_path=None, text=None):
        self.pdf_path = pdf_path
        self.nlp = spacy.load('en_core_web_sm')
        self.text = text

    def extract_text_from_pdf(self):
        with open(self.pdf_path, "rb") as file:
            pdf = PdfReader(file)
            text = pdf.pages[0].extract_text()
        return text

    def extract_section(self, section_title):
        doc = self.nlp(self.text)
        for ent in doc.ents:
            if section_title.lower() in ent.label_.lower():
                return ent.text
        return None
    
    def preprocess_text(self, text=None):
        self.text = text if text else self.text
        self.text = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        self.text = self.text.lower()
        return self.text
    
    def remove_blank_lines(self, text):
        lines = text.splitlines()
        non_blank_lines = [line.strip() for line in lines if line.strip()]
        return "\n".join(non_blank_lines)