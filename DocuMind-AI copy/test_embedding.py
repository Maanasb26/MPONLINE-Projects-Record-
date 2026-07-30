from rag.embeddings import generate_embedding

text = "Python is a programming language."

embedding = generate_embedding(text)

print(type(embedding))
print(len(embedding))
print(embedding[:10])