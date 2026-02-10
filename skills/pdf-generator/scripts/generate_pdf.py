import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(input_file, output_file):
    try:
        c = canvas.Canvas(output_file, pagesize=letter)
        width, height = letter
        text_object = c.beginText(40, height - 40)
        text_object.setFont("Helvetica", 12)

        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Simple text wrapping could be added here for better formatting
                text_object.textLine(line.strip())

        c.drawText(text_object)
        c.showPage()
        c.save()
        print(f"Successfully generated {output_file}")
    except Exception as e:
        print(f"Error generating PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_pdf.py <input_file> <output_file>")
        sys.exit(1)
    
    generate_pdf(sys.argv[1], sys.argv[2])
