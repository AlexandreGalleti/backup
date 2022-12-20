   
from tkinter import *
from tkinter import filedialog 
import os
import shutil

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
    destino = r'C:\Users\A.Galleti\Desktop\snoop'
    filename = filedialog.askopenfilename(initialdir = "/",    
        title = "Selecione um arquivo", 
        filetypes = (("Text files", "*.txt*"), 
        ("all files", "*.*"))) 
    shutil.copy(filename, destino)
    
    label_file_explorer.configure(text="Arquivo selecionado: "+filename) 

    
    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------       
button_explore = Button(window, text = "Selecionar Banco", command = browseFiles)  
   
button_exit = Button(window, text = "Sair", command = exit)  

button_explore.grid(column = 2, row = 2) 
   
button_exit.grid(column = 2,row = 3) 



window.mainloop() 




