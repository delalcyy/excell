import PyPDF2

def read_pdf(file_path, page_number):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        if page_number <= len(reader.pages):
            page = reader.pages[page_number - 1]
            return page.extract_text()
        else:
            return "Sayfa numarası geçersiz."
