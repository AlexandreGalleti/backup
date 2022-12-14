from cgitb import text
from platform import python_branch
from sqlite3 import Row
import tkinter as tk
import clipboard
from colorama import Fore
import pyautogui
import webbrowser
import time


my_w = tk.Tk()
my_w.geometry("350x350")
my_w.title("atalho de suporte")
global data


e1 = tk.Text(my_w, font=20, height=4, width=28, bg='white')
e1.grid(row=0, column=1, columnspan=4)


def select_all():
    global data 
    pyautogui.hotkey('win','r')
    pyautogui.typewrite('temp')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('DEL')



def whatsweb_select():
    global data
    webbrowser.open("https://web.whatsapp.com")


def copy_select():
    global data
    pyautogui.hotkey('win')
    pyautogui.typewrite('AnyDask')
    pyautogui.hotkey('enter')


def paste_select():
    global data
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')


def team_select():
    global data
    pyautogui.hotkey('win')
    pyautogui.typewrite('TeamViewer')
    pyautogui.hotkey('enter')


def visual_select():
    global data
    pyautogui.hotkey('win')
    pyautogui.hotkey('v', 's', 'c')
    pyautogui.hotkey('enter')


def whatsapp_select():
    global data
    pyautogui.hotkey('win')
    pyautogui.typewrite('WhatsApp')
    pyautogui.hotkey('enter')


def chamado_select():
    global data
    webbrowser.open('https://suporte.hifuzion.com.br')
    time.sleep(3)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.typewrite('hoje o cliente/a solicitou suporte')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.typewrite('chamado feito pelo cliente/a:(mensagem do cliente)')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    pyautogui.typewrite(
        'o metodo ultilizado para a corrção do problema foi:(como foi resolvido)')


b1 = tk.Button(my_w, text='LImpar cache', command=lambda: select_all(),
               font=20, bg='lightyellow')
b1.grid(row=1, column=1, padx=2, pady=5)

b2 = tk.Button(my_w, text='whats web', command=lambda: whatsweb_select(),
               font=20, bg='lightgreen')
b2.grid(row=1, column=2, padx=2, pady=5,)

b3 = tk.Button(my_w, text='Colar', command=lambda: paste_select(),
               font=20, bg='lightyellow')
b3.grid(row=1, column=3, padx=2, pady=5,)

b4 = tk.Button(my_w, text='AnyDesk', command=lambda: copy_select(),
               font=20, bg='lightblue')
b4.grid(row=2, column=1, padx=2, pady=5, )

b5 = tk.Button(my_w, text='TeamViwer', command=lambda: team_select(),
               font=20, bg='lightblue')
b5.grid(row=2, column=2, padx=2, pady=5, )

b6 = tk.Button(my_w, text='VSC', command=lambda: visual_select(),
               font=20, bg='lightblue')
b6.grid(row=2, column=3, padx=2, pady=5, )

b7 = tk.Button(my_w, text='WhatsApp', command=lambda: whatsapp_select(),
               font=20, bg='lightgreen')
b7.grid(row=3, column=2, padx=2, pady=5,)

b8 = tk.Button(my_w, text='Abrir chamado', command=lambda: chamado_select(),
               font=20, bg='cyan')
b8.grid(row=5, column=2, padx=3, pady=5, )


my_w.mainloop()
