   
from tkinter import *
from tkinter import filedialog 
import os
import shutil
from os import mkdir, chdir, getcwd, path
import os.path

#configuração da janela
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
window = Tk() 
   
window.title('Selecione o Banco') 
   
window.geometry("300x300") 
   
window.config(background = "white") 
   
label_file_explorer = Label(window,  text = "selecione o banco para o Backup", width = 100, height = 4, fg = "blue") 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#definições dos buttom
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

global data
   
def browseFiles(): 
    destino = r'C:\Users\A.Galleti\Desktop\Backup_hifuzion'
    filename = filedialog.askopenfilename(initialdir = "/",    
        title = "Selecione um arquivo", 
        filetypes = (("Text files", "*.txt*"), 
        ("all files", "*.*"))) 
    shutil.copy(filename, destino)
    label_file_explorer.configure(text="Arquivo selecionado: "+filename) 


def check():
    global data 
    pas = 'Backup_hifuzion'

    cam = path.join(path.expanduser('~'), 'Desktop')
    chdir(cam)

    if os.path.isdir(pas):
        print(F'A pasta "{pas}" já existe em Desktop!')

    else:
        mkdir(pas)
        cam2 = cam + '\\' + pas
        chdir(cam2)
        print(getcwd)
    
    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------       
button_explore = Button(window, text = "Selecionar Banco", command = browseFiles)  
   
button_check = Button(window, text = "check", command = check )

button_exit = Button(window, text = "Sair", command = exit)  


button_check.grid(column = 2,row = 2)

button_explore.grid(column = 2, row = 3) 

button_exit.grid(column = 2,row = 4) 



window.mainloop() 




