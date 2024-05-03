from extractor import ResumeExtractor

def get_skills(resume_path):
    extractor = ResumeExtractor(resume_path)
    education = extractor.extract_section("SKILLS")
    return education