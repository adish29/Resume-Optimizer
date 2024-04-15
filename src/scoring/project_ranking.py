import os
from sentence_transformers import SentenceTransformer, util

class ProjectRanker:
    def __init__(self, project_dir, query):
        self.project_dir = project_dir
        self.query = query
        self.model = SentenceTransformer('sentence-transformers/msmarco-distilbert-base-tas-b')

    def rank_projects(self):
        # Create a dictionary where keys are project names and values are project descriptions
        projects = {}
        for i, filename in enumerate(os.listdir(self.project_dir), start=1):
            with open(os.path.join(self.project_dir, filename), 'r') as file:
                projects[f'project{i}'] = file.read()

        # Encode query and documents
        query_emb = self.model.encode(self.query)
        doc_emb = {project_name: self.model.encode(project_content) for project_name, project_content in projects.items()}

        # Compute dot score between query and all document embeddings
        scores = {project_name: util.dot_score(query_emb, emb)[0].cpu().item() for project_name, emb in doc_emb.items()}

        # Sort by decreasing score
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        # Return a list of project names in ranked order
        ranked_projects = [project_name for project_name, _ in sorted_scores]

        return ranked_projects
