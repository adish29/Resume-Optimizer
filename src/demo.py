from src.tests.test_jd import JDTester
from src.tests.test_general import ResumeTester

resume_path = r'D:\Capstone\Resume-Optimizer\resume_samples\Adish_Devendra_Pathare_latest.pdf'
jd_path = r'D:\Capstone\Resume-Optimizer\job_descriptions\jd1.txt'

jd_tester = JDTester(jd_path)
resume_tester = ResumeTester(resume_path)

jd_text = jd_tester.get_plain_text()
resume_text = resume_tester.get_plain_text()

print(jd_text)
print("=====================================")
print(resume_text)


