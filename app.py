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
        self.system_title()
        self.system_sub_title()

    def layout_config(self):
        self.title("Sistema de Gestão de Clientes")
        self.geometry("700x500")

    def appearance(self):
        self.lb_apm = ctk.CTkLabel(self,text='Tema', bg_color='transparent',text_color=['#000','#fff']).place(x=50,y=430)
        self.opt_apm= ctk.CTkOptionMenu(self,values=['Light','Dark','System'],command=self.change_apm).place(x=50,y=460)

    def change_apm(self,new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def system_title(self):
        frame = ctk.CTkFrame(self,width=700,height=50,corner_radius=0,bg_color="teal",fg_color='teal').place(x=0,y=10)
        title = ctk.CTkLabel(frame,text='Sistema de Gestão de Clientes',font=('Century Gothic bold',24),text_color='#fff')

    def system_sub_title(self):
        span = ctk.CTkLabel(self,text='Por favor, preencha todos os campos do formulário!',font=('Century Gothic bold',16),text_color=['#000','#fff']).place(x=50,y=70)

if __name__=="__main__":
    app = App()
    app.mainloop()
