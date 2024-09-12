import  customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import openpyxl, xlrd
import pathlib
from openpyxl import Workbook

ctk.set_appearance_mode("System");
ctk.set_default_color_theme("blue");

class App(ctk.CTk):
    def __init__(self):     
        super().__init__()
        self.layout_config()
        self.appearance()

    
    def layout_config(self):
        self.title("Sistema de Gestão de Clientes")
        self.geometry("700x500")

    def appearance(self):
        self.lb_apm = ctk.CTkLabel(self,text='Tema', bg_color='transparent',text_color=['#000','#fff']).place(x=50,y=430)
        self.opt_apm= ctk.CTkOptionMenu(self,values=['Light','Dark','System'],command=self.change_apm).place(x=50,y=460)


    def change_apm(self,new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__=="__main__":
    app = App()
    app.mainloop()
