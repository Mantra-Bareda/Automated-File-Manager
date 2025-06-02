from tkinter import filedialog
import customtkinter as ctk
import shutil as sh
import os


## Folder select
## Checkbox (Move or copy)
## Destination select
## Press run

fol_path = "" 
des_path = ""

def get_list(p):
    
    l = os.listdir(p)

    print(l)

    return l


def label_show(x , p):
    global fol_path , des_path
    if x == "Folder":
        lab1.configure(text = "Folder Path : "+p)
        lab1.place(x = 100 , y = 40)
        fol_path = p
        print(fol_path)
    
    else:
        lab2.configure(text = "Destination path : "+p)
        lab2.place(x = 100 , y = 100)
        des_path = p

img = []
doc = []
vid = [] 
music = [] 
zips = [] 
program = [] 
others = [] 

def organize():
    global img , doc , vid,music,zips ,program , others , fol_path , des_path
    img = []
    doc = []
    vid = [] 
    music = [] 
    zips = [] 
    program = [] 
    others = [] 
    if fol_path == "":
        return None
    
    if des_path == "":
        des_path = fol_path

    w = mv_cp.get()
    w = True if w==1 else False
    print(fol_path)
    files_in_folder = get_list(fol_path)

    datas = {"img": (".png" , ".jpg" , ".jpeg" , ".webp"),
             "doc" : (".docx" , ".xlsx" , ".pdf" , ".txt"),
             "vid" : (".mp4" , ".mkv" , ".avi" , ".mov"),
             "music" : (".mp3" , ".wav"),
             "zips" : (".zip" , ".7z" , ".rar" , ".tar"),
             "program" : (".exe" , ".msi"),
             "others" : ()}
    
    folder_index = {"img":"Images" , "doc":"Documents" , "vid":"Videos" , "music":"Music" , "zips":"Compress" , "program":"Programm" , "others":"Others"}

    list_index = {"img":img , "doc":doc , "vid":vid , "music":music , "zips":zips , "program":program , "others":others}

    if w:
        for i in files_in_folder:
            for j in datas:
                if i.endswith(datas[j]):
                    list_index[j].append(i)
                    break
            else:
                list_index["others"].append(i)
        
        for i in folder_index:
            path_to_copy = os.path.join(des_path,folder_index[i])
            for j in list_index[i]:
                if os.path.exists(path_to_copy):
                    pass
                else:
                    os.mkdir(path_to_copy)
                sh.move(os.path.join(fol_path , j) , path_to_copy)

    else:   

        for i in files_in_folder:
            for j in datas:
                if i.endswith(datas[j]):
                    list_index[j].append(i)
                    break
            else:
                list_index["others"].append(i)
        
        for i in folder_index:
            path_to_copy = os.path.join(des_path,folder_index[i])
            for j in list_index[i]:
                if os.path.exists(path_to_copy):
                    pass
                else:
                    os.mkdir(path_to_copy)
                sh.copy(os.path.join(fol_path , j) , path_to_copy)      

def select_folder(x):
    path_1 = filedialog.askdirectory()

    if x == "Folder":
        print("x === ",x)
        label_show(x , path_1)

    else:
        print("x === ",x)
        label_show(100 , path_1)



def main():
    ## Global
    global lab1 , lab2 , win , mv_cp

    ## Main Window Initialization
    win = ctk.CTk()
    win.geometry("400x300+100+100")
    win.title("Automated File Organizer")
    win.configure(fg_color = "#36454F")


    ## Labels
    lab1 = ctk.CTkLabel(win , text_color="White")
    lab2 = ctk.CTkLabel(win, text_color="White")

    ## Buttons
    folder_path = ctk.CTkButton(win , width =  200 , text ="Select Folder" , command=lambda :[select_folder("Folder")] , font=("Arial", 12, "bold"))
    destination_path = ctk.CTkButton(win , width =  200 , text ="Select Destination Folder" , command=lambda :[select_folder("x")], font=("Arial", 12, "bold"))
    run = ctk.CTkButton(win , width =  200 , text ="Organize Them !!" , command=lambda :[organize()], font=("Arial", 12, "bold"))

    ## Checkbox 
    mv_cp = ctk.CTkCheckBox(win ,text_color="White" , border_color="White", text = "Move All Files", font=("Arial", 12, "bold"))


    folder_path.place(x = 100 , y = 10)
    destination_path.place(x = 100 , y = 70)
    run.place(x = 100 , y = 200)

    mv_cp.place(x = 145 , y = 150)

    win.mainloop()

main()