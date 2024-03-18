from src.resume_extractor.projects import get_projects

# Path to the resume PDF file
resume_pdf_path = r'D:\Capstone\Resume-Optimizer\resume_samples\Adish_Devendra_Pathare_latest.pdf'
projects = get_projects(resume_pdf_path)
print("Projects:", projects)