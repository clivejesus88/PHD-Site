import PyPDF2
import os

def read_pdf_content(pdf_path):
    """Extract text content from PDF file"""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

def main():
    # Path to your PDF files
    pdf_files = [
        "PHD-FNI-Annual-Report-2024-25-Comprehensive.docx_20260102_101440_0000.pdf",
        "Share ✨PHD'S FNI FINAL CONSTITUTION 🫴.pdf"
    ]
    
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            print(f"\n=== Reading {pdf_file} ===")
            content = read_pdf_content(pdf_file)
            if content:
                # Save content to text file for easier processing
                output_file = pdf_file.replace('.pdf', '.txt')
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Content saved to {output_file}")
                print(f"Total characters: {len(content)}")
                print(f"First 500 characters:\n{content[:500]}")
        else:
            print(f"File not found: {pdf_file}")

if __name__ == "__main__":
    main()
