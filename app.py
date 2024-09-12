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
        self.system_main()

    def layout_config(self):
        self.title("Sistema de Gestão de Clientes")
        self.geometry("700x500")

    def appearance(self):
        self.lb_apm = ctk.CTkLabel(self,text='Tema', bg_color='transparent',text_color=['#000','#fff']).place(x=50,y=430)
        self.opt_apm= ctk.CTkOptionMenu(self,values=['Light','Dark','System'],command=self.change_apm).place(x=50,y=460)

    def change_apm(self,new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def system_title(self):
        frame = ctk.CTkFrame(self,width=700,height=50,corner_radius=0,bg_color="teal",fg_color='teal').place(x=0,y=12)
        title = ctk.CTkLabel(frame, text='Sistema de Gestão de Clientes', font=('Century Gothic bold', 24), text_color='#fff')
        title.pack(pady=20)

    def system_sub_title(self):
        span = ctk.CTkLabel(self,text='Por favor, preencha todos os campos do formulário!',font=('Century Gothic bold',16),text_color=['#000','#fff']).pack(pady=20)

    def system_main(self):

        lb_name = ctk.CTkLabel(self,text='Nome',font=('Century Gothic bold',16),text_color=['#000','#fff']).place(x=50,y=120)
        name_entry = ctk.CTkEntry(self,width=350,font=("Century Gohtic bold",16),bg_color='transparent',fg_color='transparent').place(x=50,y=150)

        lb_contact = ctk.CTkLabel(self,text='Telefone',font=('Century Gothic bold',16),text_color=['#000','#fff']).place(x=420,y=120)
        contact_entry = ctk.CTkEntry(self,width=200,font=("Century Gohtic bold",16),bg_color='transparent',fg_color='transparent').place(x=420,y=150)

        lb_address = ctk.CTkLabel(self,text='Endereço',font=('Century Gothic bold',16),text_color=['#000','#fff']).place(x=50,y=180)
        address_entry = ctk.CTkEntry(self,width=200,font=("Century Gohtic bold",16),bg_color='transparent',fg_color='transparent').place(x=50,y=200)

        lb_age_ = ctk.CTkLabel(self,text='Idade',font=('Century Gothic bold',16),text_color=['#000','#fff']).place(x=260,y=180)
        age_entry = ctk.CTkEntry(self,width=150,font=("Century Gohtic bold",16),bg_color='transparent',fg_color='transparent').place(x=260,y=200)


        lb_gender = ctk.CTkLabel(self,text='Gênero',font=('Century Gothic bold',16),text_color=['#000','#fff']).place(x=420,y=180)
        gender_box = ctk.CTkComboBox(self,values=['Masculino','Feminino'],width=100,font=("Century Gohtic bold",14)).place(x=420,y=200)


        lb_obs = ctk.CTkLabel(self,text='Observações',font=('Century Gothic bold',16),text_color=['#000','#fff']).place(x=50,y=230)
        options_text_box = ctk.CTkTextbox(self,width=500,height=150,font=("arial",18),fg_color='transparent',border_color='#aaa',border_width=2).place(x=50,y=260)



if __name__=="__main__":
    app = App()
    app.mainloop()
