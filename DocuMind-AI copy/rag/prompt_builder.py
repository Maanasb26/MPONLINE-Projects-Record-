def build_prompt(context_chunks, question):

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are DocuMind AI, an expert document assistant.

Answer ONLY using the information present in the provided context.

Rules:
1. Do NOT use outside knowledge.
2. If the answer exists, quote it accurately.
3. If multiple values exist, mention all of them.
4. If the answer is not found, reply exactly:
"I couldn't find that information in the uploaded document."

=========================
DOCUMENT CONTEXT
=========================

{context}

=========================
USER QUESTION
=========================

{question}

=========================
ANSWER
=========================
"""

    return prompt