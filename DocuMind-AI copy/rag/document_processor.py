from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import generate_embedding
from rag.vector_store import VectorStore


class DocumentProcessor:

    def process_pdf(self, pdf_path):

        print("Loading PDF...")

        text = load_pdf(pdf_path)

        print("Chunking...")

        chunks = chunk_text(text)

        print("Generating Embeddings...")

        embeddings = [
            generate_embedding(chunk)
            for chunk in chunks
        ]

        print("Saving Vector Store...")

        store = VectorStore()

        store.add_embeddings(
            embeddings,
            chunks
        )

        store.save()

        print("Done.")

        return len(chunks)