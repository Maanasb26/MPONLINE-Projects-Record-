from rag.retriever import Retriever
from rag.prompt_builder import build_prompt
from rag.gemini_client import generate_answer


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()

    def ask(self, question):

        chunks = self.retriever.retrieve(question)

        prompt = build_prompt(chunks, question)

        answer = generate_answer(prompt)

        return answer