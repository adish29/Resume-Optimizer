from extractor import ResumeExtractor

def get_experience(resume_path):
    extractor = ResumeExtractor(resume_path)
    education = extractor.extract_section("EXPERIENCE")
    return education