from src.resume_extractor.extractor import ResumeExtractor

class ResumeTester:
    def __init__(self, resume_pdf_path):
        self.resume_pdf_path = resume_pdf_path
        self.extractor = ResumeExtractor(self.resume_pdf_path)

    def get_preprocessed_text(self):
        text = self.extractor.extract_text_from_pdf()
        return self.extractor.preprocess_text(text)

    def get_plain_text(self):
        preprocessed_text = self.get_preprocessed_text()
        return self.extractor.remove_blank_lines(preprocessed_text)