import sys
import pdfplumber

def read_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
            print(text)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 read_pdf.py <pdf_path>")
        sys.exit(1)

    read_pdf(sys.argv[1])
