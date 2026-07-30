from rag.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "What is Machine Learning?"
)

print()

print("="*60)

print("RETRIEVED CHUNKS")

print("="*60)

for i, chunk in enumerate(results):

    print(f"\nChunk {i+1}\n")

    print(chunk)