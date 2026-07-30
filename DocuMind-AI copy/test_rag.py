from rag.retriever import Retriever
from rag.prompt_builder import build_prompt
from rag.gemini_client import generate_answer

question = "What is Machine Learning?"

retriever = Retriever()

chunks = retriever.retrieve(question)

prompt = build_prompt(chunks, question)

answer = generate_answer(prompt)

print("=" * 60)
print("QUESTION")
print("=" * 60)
print(question)

print("\n" + "=" * 60)
print("RETRIEVED CHUNKS")
print("=" * 60)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print(chunk)

print("\n" + "=" * 60)
print("FINAL ANSWER")
print("=" * 60)
print(answer)