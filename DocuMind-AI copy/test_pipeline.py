from rag.rag_pipeline import RAGPipeline

pipeline = RAGPipeline()

answer = pipeline.ask(
    "What is Machine Learning?"
)

print(answer)
