from src.scoring.keywords import KeywordExtractor
from src.scoring.score_calculator import ScoreCalculator
from src.scoring.similarity import SentenceEmbedder
from src.tests.test_jd import JDTester
from src.tests.test_general import ResumeTester

class CombinedScoreCalculator:
    def __init__(self, jd_text=None, resume_text=None, keyword_score=None, sentence_similarity_score=None):
        self.jd_text = jd_text
        self.resume_text = resume_text
        self.keyword_score = keyword_score
        self.sentence_similarity_score = sentence_similarity_score

    def calculate_score(self):
        if self.keyword_score is None:
            jd_keywords = KeywordExtractor(self.jd_text).extract_keywords()
            keyword_score_calculator = ScoreCalculator(jd_keywords, self.resume_text)
            self.keyword_score = keyword_score_calculator.calculate_score()

        if self.sentence_similarity_score is None:
            sentence_embedder = SentenceEmbedder(self.jd_text, self.resume_text)
            self.sentence_similarity_score = sentence_embedder.get_similarity()

        combined_score = self.keyword_score + self.sentence_similarity_score
        return combined_score
