import faiss
import numpy as np
import pickle
import os


class VectorStore:

    def __init__(self):

        self.dimension = 3072

        self.index = faiss.IndexFlatL2(self.dimension)

        self.chunks = []

    def add_embeddings(self, embeddings, chunks):

        vectors = np.array(embeddings).astype("float32")

        self.index.add(vectors)

        self.chunks.extend(chunks)

    def save(self):

        os.makedirs("vector_db", exist_ok=True)

        faiss.write_index(
            self.index,
            "vector_db/faiss.index"
        )

        with open(
            "vector_db/chunks.pkl",
            "wb"
        ) as f:

            pickle.dump(self.chunks, f)

    def load(self):

        self.index = faiss.read_index(
            "vector_db/faiss.index"
        )

        with open(
            "vector_db/chunks.pkl",
            "rb"
        ) as f:

            self.chunks = pickle.load(f)