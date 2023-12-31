""" this funtion will take 3 parameters, 
1 is the list, 
2 is the file name that the user choose
3 is the folder path
and it will create the txt document."""


def create_txt_file(lst, file_name, save_doc_folder_path):
    file_list = lst
    with open(f"{save_doc_folder_path}/{file_name}.txt", "w", encoding="utf-8") as txt_file:

        for index, document in enumerate(file_list):
            files = f"{index + 1} - {document}"
            txt_file.write(files + "\n")

    txt_file.close()