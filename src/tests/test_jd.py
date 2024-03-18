from src.resume_extractor.extractor import ResumeExtractor
from src.jd_extractor.extractor import JDExtractor

class JDTester:
    def __init__(self, jd_path):
        self.jd_path = jd_path
        self.jd_extractor = JDExtractor(self.jd_path)
        self.jd = self.jd_extractor.extract()
        self.extractor = ResumeExtractor(text=self.jd)

    def get_preprocessed_text(self):
        return self.extractor.preprocess_text()

    def get_plain_text(self):
        preprocessed_text = self.get_preprocessed_text()
        return self.extractor.remove_blank_lines(preprocessed_text)