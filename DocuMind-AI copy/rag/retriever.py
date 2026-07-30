import numpy as np

from rag.embeddings import generate_embedding
from rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.store = VectorStore()
        self.store.load()

    def retrieve(self, question, top_k=5):

        question_embedding = generate_embedding(question)

        query = np.array([question_embedding], dtype="float32")

        distances, indices = self.store.index.search(query, top_k)

        results = []

        print("\n" + "=" * 70)
        print("RETRIEVER DEBUG")
        print("=" * 70)
        print("Question:", question)

        for i, idx in enumerate(indices[0]):

            print("\n" + "-" * 70)
            print(f"Chunk {i+1}")
            print(f"Distance: {distances[0][i]}")
            print(self.store.chunks[idx])

            results.append(self.store.chunks[idx])

        print("=" * 70 + "\n")

        return results