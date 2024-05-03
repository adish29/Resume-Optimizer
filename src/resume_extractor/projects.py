from extractor import ResumeExtractor

def get_projects(resume_path):
    extractor = ResumeExtractor(resume_path)
    education = extractor.extract_section("PROJECTS")
    return education