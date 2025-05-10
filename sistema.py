import customtkinter as ctk
from tkinter import messagebox
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("usuario")
password = os.getenv("senha")

COLOR_PRIMARY = "#2b2b2b"       # Cor principal (escuro)
COLOR_SECONDARY = "#3a7ebf"     # Azul principal 
COLOR_HOVER = "#325882"         # Azul mais escuro (hover)
COLOR_LIGHT_BG = "#f5f5f5"      # Fundo claro
COLOR_ENTRY_BG = "#e0e0e0"      # Fundo do campo de entrada
COLOR_ERROR = "#e74c3c"         # Vermelho para erros
COLOR_SUCCESS = "#2ecc71"       # Verde para sucesso

def Verificador(input_user, input_senha):
    usuario = input_user.get()
    senha = input_senha.get()
    if usuario == user and senha == password:
        pagina_login.destroy()
        sistema()
    elif usuario == "":
        messagebox.showerror("Erro", "Insira o usuário", icon="warning")
    elif senha == "":
        messagebox.showerror("Erro", "Insira a senha", icon="warning")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos", icon="error")

def janela_login():
    global pagina_login
    pagina_login = ctk.CTk()
    ctk.set_appearance_mode("light")
    pagina_login.geometry("700x500")
    pagina_login.resizable(False, False)
    pagina_login.title("Página de Login")
    pagina_login.configure(bg=COLOR_LIGHT_BG)

    # Frame central 
    quadrado = ctk.CTkFrame(
        master=pagina_login, 
        width=350, 
        height=396, 
        corner_radius=15,
        fg_color="white",
        border_width=1,
        border_color="#e1e1e1"
    )
    quadrado.place(relx=0.5, rely=0.5, anchor="center")

    # Título
    label_titulo = ctk.CTkLabel(
        master=quadrado, 
        text="Login Administrativo",
        font=("Arial", 18, "bold"),
        text_color=COLOR_PRIMARY
    )
    label_titulo.place(relx=0.5, y=50, anchor="center")

    # Campos de entrada
    label_user = ctk.CTkLabel(
        master=quadrado, 
        text="USUÁRIO", 
        text_color=COLOR_PRIMARY,
        font=("Arial", 12)
    )
    label_user.place(x=50, y=100)

    input_user = ctk.CTkEntry(
        master=quadrado,
        width=250,
        height=40,
        corner_radius=8,
        fg_color=COLOR_ENTRY_BG,
        border_width=0,
        placeholder_text="Digite o usuário"
    )
    input_user.place(x=50, y=130)

    label_senha = ctk.CTkLabel(
        master=quadrado, 
        text="SENHA", 
        text_color=COLOR_PRIMARY,
        font=("Arial", 12)
    )
    label_senha.place(x=50, y=180)

    input_senha = ctk.CTkEntry(
        master=quadrado,
        width=250,
        height=40,
        corner_radius=8,
        fg_color=COLOR_ENTRY_BG,
        border_width=0,
        show="*",
        placeholder_text="Digite a senha"
    )
    input_senha.place(x=50, y=210)

    # Botão de login
    btn_login = ctk.CTkButton(
        master=quadrado,
        text="ACESSAR SISTEMA",
        width=250,
        height=40,
        command=lambda: Verificador(input_user, input_senha),
        fg_color=COLOR_SECONDARY,
        hover_color=COLOR_HOVER,
        corner_radius=8,
        font=("Arial", 14, "bold")
    )
    btn_login.place(x=50, y=280)

    pagina_login.mainloop()

def sistema():
    main_window = ctk.CTk()
    ctk.set_appearance_mode("light")
    main_window.geometry("800x600")
    main_window.title("Sistema Escolar")
    main_window.resizable(False, False)

    # Menu lateral
    menu = ctk.CTkFrame(
        master=main_window, 
        width=250, 
        height=600,
        fg_color=COLOR_PRIMARY,
        corner_radius=0
    )
    menu.place(x=0, y=0)

    # Cabeçalho do menu
    label_titulo = ctk.CTkLabel(
        master=menu,
        text="SISTEMA ESCOLAR",
        font=("Arial", 20, "bold"),
        text_color="white"
    )
    label_titulo.place(x=20, y=40)

    # Botões do menu
    btn_style = {
        "master": main_window,
        "width": 250,
        "height": 45,
        "corner_radius": 0,
        "border_width": 0,
        "font": ("Arial", 14),
        "anchor": "w",
        "fg_color": COLOR_PRIMARY,
        "hover_color": COLOR_HOVER,
        "text_color": "white"
    }

    btn1 = ctk.CTkButton(
        **btn_style,
        text="SOLICITAÇÕES DE DOCUMENTOS"
    )
    btn1.place(x=0, y=150)

    btn2 = ctk.CTkButton(
        **btn_style,
        text="HORÁRIOS"
    )
    btn2.place(x=0, y=195)

    # Botão de sair (destaque diferente)
    btn3 = ctk.CTkButton(
        master=main_window,
        width=250,
        height=45,
        text="  SAIR",
        command=main_window.destroy,
        corner_radius=0,
        border_width=0,
        font=("Arial", 14),
        fg_color="#444444",
        hover_color=COLOR_ERROR,
        text_color="white"
    )

    btn3.place(x=0, y=560)

    main_window.mainloop()

janela_login()