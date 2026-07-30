import fitz


def load_pdf(pdf_path):

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    print("\n" + "=" * 70)
    print("PDF TEXT EXTRACTED")
    print("=" * 70)
    print(text[:5000])
    print("=" * 70 + "\n")

    return text