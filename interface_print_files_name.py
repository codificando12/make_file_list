from tkinter import *
from tkinter import filedialog
from read_folder import read_dir
from create_word import create_word_file
from create_txt import create_txt_file
from PIL import ImageTk, Image
from docx import Document

"""This function will open the folder browser for the user to choose the folder that he/she
wants to scan"""
def search_path():
    global folder_path
    folder_path = filedialog.askdirectory()
    path_label.configure(text=folder_path) #this will save the folder path in a label

def save_file_path():
    global save_folder_path
    save_folder_path = filedialog.askdirectory()
    save_path_label.configure(text=save_folder_path) #this will save the folder path in a label

"""This function will start the software and create the document"""
def start_scan():
    file_list = read_dir(folder_path)
    file_name = file_name_box.get()
    word_doc = check_word.get()
    txt_doc = check_txt.get()
    error_label = "Please Check one Option"
    succes_label = "File created"
    if  word_doc == 1 and txt_doc == 0:
        create_word_file(file_list, file_name, save_folder_path)
        erase_label = Label(root, text="                                                          ")
        erase_label.grid(row=6, column=1)
        message_label = Label(root, text=succes_label)
        message_label.grid(row=6, column=1)
    elif word_doc == 0 and txt_doc == 1:
        create_txt_file(file_list, file_name, save_folder_path)
        erase_label = Label(root, text="                                                          ")
        erase_label.grid(row=6, column=1)
        message_label = Label(root, text=succes_label)
        message_label.grid(row=6, column=1)
        print(folder_path)
        print(file_list)
    else:
        message_label = Label(root, text=error_label, fg="red")
        message_label.grid(row=6, column=1)
    
# def set_file_name():
#     global file_name
#     file_name = file_name_box.get()

folder_path = "" #save the folder path that search_path() function returns

save_folder_path = "" #save the path where the user choose to save the document

root = Tk() #start tkinter
root.title("Folder.Scanner")

check_word = IntVar()
check_txt = IntVar()

name_image = ImageTk.PhotoImage(Image.open("folderScanner.jpg"))

root.geometry("500x500") # set the window dimension
# root.resizable(False,False)

header_img = Label(root, image = name_image)
header_img.grid(row = 0, column = 0, columnspan = 3)

title_label = Label(root, text="Generate a txt or docxs with all the names file of \n specific folder")
title_label.grid(row=1, column=1)

folder_label = Label(root, text="Choose Folder\nto Scan")
folder_label.grid(row=2, column=0, padx=2, pady=2)

path_label = Label(root, bg="White", width=50)
path_label.grid(row=2, column=1)

browse_button = Button(root, text="Browse", command=search_path)
browse_button.grid(row=2, column=2, padx=6)

file_name_label = Label(root, text="Choose \nfile name")
file_name_label.grid(row=3, column=0)

file_name_box = Entry(root, width=59)
file_name_box.grid(row=3, column=1)

save_folder = Label(root, text="Choose Folder\n to Save File")
save_folder.grid(row=4, column=0, padx=2, pady=2)

save_path_label = Label(root, bg="White", width=50)
save_path_label.grid(row=4, column=1)

browse_button = Button(root, text="Browse", command=save_file_path)
browse_button.grid(row=4, column=2, padx=6)

check_word_box = Checkbutton(root, text="Word Document", variable=check_word)
check_word_box.grid(row=5, column= 1)

check_txt_box = Checkbutton(root, text="Text Document", variable=check_txt)
check_txt_box.grid(row=6, column= 1)

scan_button = Button(root, text='Scan', command=start_scan)
scan_button.grid(row = 7, column = 1, pady=10, ipadx=20)




root.mainloop()