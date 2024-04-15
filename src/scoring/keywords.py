from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class KeywordExtractor:
    def __init__(self, text):
        self.text = text
        self.tokenizer = AutoTokenizer.from_pretrained("ilsilfverskiold/tech-keywords-extractor")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("ilsilfverskiold/tech-keywords-extractor")
        self.extracted_keywords = set()

    def extract_keywords(self, max_new_tokens=20):
        inputs = self.tokenizer([self.text], return_tensors="pt")
        outputs = self.model.generate(inputs['input_ids'], max_new_tokens=max_new_tokens)
        keywords = self.tokenizer.decode(outputs[0]).replace('<s>', '').replace('</s>', '')
        keywords = [keyword.strip() for keyword in keywords.split(',') if keyword.strip()]
        self.extracted_keywords.update(keywords)
        return list(self.extracted_keywords)
