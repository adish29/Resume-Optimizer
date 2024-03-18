from extractor import ResumeExtractor

def get_education(resume_path):
    extractor = ResumeExtractor(resume_path)
    education = extractor.extract_section("EDUCATION")
    return education