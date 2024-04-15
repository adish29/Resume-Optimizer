from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class SentenceEmbedder:
    def __init__(self, sentence1, sentence2):
        self.sentences = [sentence1, sentence2]
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def get_embeddings(self):
        embeddings = self.model.encode(self.sentences)
        return embeddings

    def get_similarity(self):
        embeddings = self.get_embeddings()
        similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
        return similarity * 100

# embedder = SentenceEmbedder('Each sentence is converted','This is an example sentence')
# similarity = embedder.get_similarity()
# print(similarity)