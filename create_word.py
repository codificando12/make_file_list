from docx import Document


def create_word_file(list):
    file_list = list
    word_document = Document()
    for document in enumerate(file_list):

        file_list = f'{document[0] + 1} - {document[1]}' 
        word_document.add_paragraph(file_list)

    word_document.save("proff.docx")