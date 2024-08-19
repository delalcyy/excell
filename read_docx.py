from docx import Document

def read_docx(file_path, page_number):
    doc = Document(file_path)
    # DOCX dosyaları tek bir akış olarak saklandığı için, sayfa kavramı yoktur.
    # Bu nedenle paragraf numarasına göre işlem yapacağız.
    content = []
    for i, para in enumerate(doc.paragraphs):
        if i >= (page_number - 1) * 30 and i < page_number * 30:
            content.append(para.text)
    return "\n".join(content)




