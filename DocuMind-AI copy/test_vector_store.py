from rag.vector_store import VectorStore
from rag.embeddings import generate_embedding

texts = [
    "Python is a programming language.",
    "Machine Learning is a branch of AI.",
    "Paris is the capital of France."
]

embeddings = []

for text in texts:

    embeddings.append(
        generate_embedding(text)
    )

store = VectorStore()

store.add_embeddings(
    embeddings,
    texts
)

store.save()

print("Vector Store Saved Successfully!")