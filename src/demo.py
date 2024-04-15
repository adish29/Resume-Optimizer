import warnings
warnings.filterwarnings('ignore')

from src.tests.test_jd import JDTester
from src.tests.test_general import ResumeTester
from src.scoring.keywords import KeywordExtractor
from src.scoring.score_calculator import ScoreCalculator
from src.scoring.similarity import SentenceEmbedder
from src.scoring.combine_score import CombinedScoreCalculator
from src.scoring.project_ranking import ProjectRanker

resume_path = r'D:\Capstone\Resume-Optimizer\resume_samples\Adish_Devendra_Pathare_latest.pdf'
jd_path = r'D:\Capstone\Resume-Optimizer\job_descriptions\jd5.txt'

project_dir = r'D:\Capstone\Resume-Optimizer\project_samples'

jd_tester = JDTester(jd_path)
resume_tester = ResumeTester(resume_path)

jd_text = jd_tester.get_plain_text()
resume_text = resume_tester.get_plain_text()

jd_keywords = KeywordExtractor(jd_text).extract_keywords()
print("JD Keywords: ", jd_keywords)

keyword_score_calculator = ScoreCalculator(jd_keywords, resume_text)
keyword_score = keyword_score_calculator.calculate_score()

sentence_embedder = SentenceEmbedder(jd_text, resume_text)
sentence_similarity_score = sentence_embedder.get_similarity()

combined_score_calculator = CombinedScoreCalculator(keyword_score=keyword_score, sentence_similarity_score=sentence_similarity_score)
combined_score = combined_score_calculator.calculate_score()

print(f"Keyword Score: {keyword_score}")
print(f"Sentence Similarity Score: {sentence_similarity_score}")
print(f"Combined Score: {combined_score}")

project_ranker = ProjectRanker(project_dir, jd_text)
ranked_projects = project_ranker.rank_projects()
print("Ranked Projects: ", ranked_projects)