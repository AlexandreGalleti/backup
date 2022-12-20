   
from tkinter import *
from tkinter import filedialog 

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
    filename = filedialog.askopenfilename(initialdir = "/",    
        title = "Selecione um arquivo", 
        filetypes = (("all files"))) 
       
    
    label_file_explorer.configure(text="Arquivo selecionado: "+filename) 


def copy():
    global data



#configuração dos buttom
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
       
button_explore = Button(window, text = "Selecionar Banco", command = browseFiles)  
   
button_exit = Button(window, text = "Sair", command = exit)  
   
button_explore.grid(column = 2, row = 2) 
   
button_exit.grid(column = 2,row = 3) 


window.mainloop() 
