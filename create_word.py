from docx import Document
import os

""" this funtion will take 3 parameter, 
1 is the list, 
2 is the file name that the user choose
3 is the folder path
and it will create the word document."""

def create_word_file(lst, file_name, save_doc_folder_path):
    file_list = lst
    word_document = Document()
    for document in enumerate(file_list):

        file_list = f'{document[0] + 1} - {document[1]}' 
        word_document.add_paragraph(file_list)

    save_path = os.path.join(save_doc_folder_path, f"{file_name}.docx")

    word_document.save(save_path)