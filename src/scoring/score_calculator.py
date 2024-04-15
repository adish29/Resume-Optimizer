class ScoreCalculator:
    def __init__(self, jd_keywords, resume_text):
        self.jd_keywords = jd_keywords
        self.resume_text = resume_text

    def calculate_score(self):
        found_keywords = [keyword for keyword in self.jd_keywords if keyword.lower() in self.resume_text]
        score = len(found_keywords) / len(self.jd_keywords) * 100
        return score

# Usage
# score_calculator = ScoreCalculator(jd_keywords, resume_text)
# score = score_calculator.calculate_score()
# print(score)