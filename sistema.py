import customtkinter as ctk
from tkinter import messagebox
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("user")
password = os.getenv("password")

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
    main_window.title("Sistema Escolar")
    main_window.attributes("-fullscreen", True)
    main_window.resizable(False, False)

    # Menu lateral
    menu = ctk.CTkFrame(
        master=main_window, 
        fg_color=COLOR_PRIMARY,
        corner_radius=0
    )
    menu.place(x=0, y=0, relwidth=0.25 , relheight=1)


    frame_conteudo = ctk.CTkFrame(
        master=main_window,
        width=1030,
        height=720,
        fg_color="white"
    )
    frame_conteudo.place(x=250, y=0,relwidth=1, relheight=1)

    msgEntrada =ctk.CTkLabel(master=frame_conteudo, text="BEM VINDO ADMIN", font=("Arial",20, "bold"))
    msgEntrada.place(x=450, y=250)
    
    def limparTela():
        for widget in frame_conteudo.winfo_children():
            widget.destroy()
    
    def tela_documentos():
        limparTela()
        titulo = ctk.CTkLabel(master=frame_conteudo, text="SOLICITAÇÕES", font=("Arial", 20, "bold"))
        titulo.place(x=60, y=10)
        
        frame_pedidos = ctk.CTkFrame(
            master=frame_conteudo,
            fg_color="white",
            border_width=1,
            border_color="#e1e1e1",
            width=920,
            height=500
        )
        frame_pedidos.place(x=40, y=150)
        # Adicione mais widgets aqui

    def tela_registrar_horarios():
        limparTela()
        cursos = ["INFORMÁTICA", "NUTRIÇÃO", "MEIO AMBIENTE", "ADMINISTRAÇÃO", "INTEGRAL"]
        turmas = ["TURMA A", "TURMA B", "TURMA C", "TURMA D"]
        turmas_integral = ["TURMA A", "TURMA B", "TURMA C", "TURMA D", "TURMA E", "TURMA F", "TURMA G", "TURMA H"]
        series = ["1º ANO", "2º ANO", "3º ANO"]
        
        # horarios
        horarios_padrao = ["1º", "2º", "3º", "4º", "5º", "6º"]
        horarios_integral = ["1º", "2º", "3º", "4º", "5º", "6º", "7º", "8º"]
        horarios_atuais = horarios_padrao

        # Título
        titulo = ctk.CTkLabel(master=frame_conteudo, text="REGISTRAR HORÁRIOS", font=("Arial", 20, "bold"))
        titulo.place(x=60, y=10)

        # Frame para os horarios
        frame_selecoes = ctk.CTkFrame(
            master=frame_conteudo, 
            fg_color="white",
            border_width=1,
            border_color="#e1e1e1"
        )
        frame_selecoes.place(relx=0.15, rely=0.1, relwidth=0.5, relheight=0.1)

        # seleção ensino
        selecao_ensino = ctk.CTkComboBox(
            master=frame_selecoes,
            values=cursos,
            font=("Arial", 12),
            width=140,
            state="readonly"
        )
        selecao_ensino.set(cursos[0])
        selecao_ensino.place(relx=0.14, rely=0.35)

        #seleção turma
        selecao_turma = ctk.CTkComboBox(
            master=frame_selecoes,
            values=turmas,
            font=("Arial", 12),
            width=140,
            state="readonly"
        )
        selecao_turma.set(turmas[0])
        selecao_turma.place(relx=0.47, rely=0.35)

        #seleção serie
        selecao_serie = ctk.CTkComboBox(
            master=frame_selecoes,
            values=series,
            font=("Arial", 12),
            width=140,
            state="readonly"
        )
        selecao_serie.set(series[0])
        selecao_serie.place(relx=0.78, rely=0.35)

        # Labels das seleções
        ctk.CTkLabel(master=frame_selecoes, text="ENSINO:", font=("Arial", 14,"bold")).place(relx=0.04, rely=0.35)
        ctk.CTkLabel(master=frame_selecoes, text="TURMA:", font=("Arial", 14,"bold")).place(relx=0.37, rely=0.35)
        ctk.CTkLabel(master=frame_selecoes, text="SÉRIE:", font=("Arial", 14,"bold")).place(relx=0.7, rely=0.35)

        # Frame para tabela 
        frame_tabela = ctk.CTkScrollableFrame(
            master=frame_conteudo,
            fg_color="white",
            border_width=1,
            border_color="#e1e1e1"
        )
        frame_tabela.place(relx=0.15, rely=0.25, relwidth=0.6, relheight=0.6)

        def criar_tabela(horarios):
            # Limpa o frame da tabela
            for widget in frame_tabela.winfo_children():
                widget.destroy()
            
            # Configuração da tabela
            dias_semana = ["SEGUNDA", "TERÇA", "QUARTA", "QUINTA", "SEXTA"]
            largura_coluna = 170
            altura_linha = 90

            # Cabeçalhos das colunas (dias da semana)
            for col, dia in enumerate(dias_semana):
                header = ctk.CTkLabel(
                    master=frame_tabela,
                    text=dia,
                    font=("Arial", 14, "bold"),
                    width=largura_coluna-10,
                    height=40,
                    corner_radius=5,
                    fg_color=COLOR_SECONDARY,
                    text_color="white"
                )
                header.grid(row=0, column=col+1, padx=10,pady=10)

            # Linhas da tabela (horários)
            for row, horario in enumerate(horarios, start=1):
                # Label do horário
                lbl_horario = ctk.CTkLabel(
                    master=frame_tabela,
                    text=f"{horario}º Horário",
                    font=("Arial", 12, "bold"),
                    width=110,
                    height=altura_linha-10,
                    corner_radius=5,
                    fg_color=COLOR_ENTRY_BG
                )
                lbl_horario.grid(row=row, column=0, padx=10, pady=10)

                # Campos para cada dia
                for col in range(len(dias_semana)):
                    frame_celula = ctk.CTkFrame(
                        master=frame_tabela,
                        width=largura_coluna-10,
                        height=altura_linha-10,
                        fg_color="#f8f8f8",
                        corner_radius=5
                    )
                    frame_celula.grid(row=row, column=col+1, padx=5, pady=5)
                    frame_celula.grid_propagate(False)
                    
                    # Campo matéria
                    entry_materia = ctk.CTkEntry(
                        master=frame_celula,
                        placeholder_text="Matéria",
                        width=largura_coluna-20,
                        height=30,
                        font=("Arial", 14)
                    )
                    entry_materia.pack(pady=(10, 5), padx=5)
                    
                    # Campo professor
                    entry_professor = ctk.CTkEntry(
                        master=frame_celula,
                        placeholder_text="Professor",
                        width=largura_coluna-20,
                        height=30,
                        font=("Arial", 14)
                    )
                    entry_professor.pack(pady=5, padx=5)

        # Criar tabela inicial
        criar_tabela(horarios_padrao)

        def mudar_ensino(escolha):
            if escolha == "INTEGRAL":
                selecao_turma.configure(values=turmas_integral)
                selecao_turma.set(turmas_integral[0])
                horarios_atuais = horarios_integral
            else:
                selecao_turma.configure(values=turmas)
                selecao_turma.set(turmas[0])
                horarios_atuais = horarios_padrao
            criar_tabela(horarios_atuais)

        selecao_ensino.configure(command=mudar_ensino)

        # Botão para salvar 
        btn_salvar = ctk.CTkButton(
            master=frame_conteudo,
            text="SALVAR HORÁRIOS",
            width=150,
            height=35,
            fg_color=COLOR_SECONDARY,
            hover_color=COLOR_HOVER,
            font=("Arial", 12, "bold"),
            corner_radius=8,
            command=lambda: salvar_horario()
        )
        btn_salvar.place(relx=0.65, rely=0.85)

        def salvar_horario():
            # salvar no banco de dados
            messagebox.showinfo("Sucesso", "Horários salvo com sucesso!")


    def tela_registrar_boletins():
        limparTela()
        
        # Cursos
        cursos = ["INFORMÁTICA", "NUTRIÇÃO", "ADMINISTRAÇÃO", "INTEGRAL"]
        
        # Turmas 
        turmas = ["TURMA A", "TURMA B", "TURMA C", "TURMA D"]
        turmas_integral = turmas + ["TURMA E", "TURMA F", "TURMA G", "TURMA H"]
        
        # Matérias por curso 
        materias_info = ["PROGRAMAÇÃO", "REDES", "BANCO DE DADOS", "MATEMÁTICA", "PORTUGUÊS"]
        materias_nutri = ["NUTRIÇÃO BÁSICA", "DIETÉTICA", "MICROBIOLOGIA", "PORTUGUÊS"]
        materias_adm = ["CONTABILIDADE", "GESTÃO", "MAT. FINANCEIRA", "PORTUGUÊS"]
        materias_integral = ["PORTUGUÊS", "MATEMÁTICA", "CIÊNCIAS", "HISTÓRIA", "GEOGRAFIA"]
        
        series = ["1º ANO", "2º ANO", "3º ANO"]
        
        # Variável para controlar as matérias atuais
        materias_atuais = materias_info  

        
        # Título 
        titulo = ctk.CTkLabel(
            master=frame_conteudo, 
            text="BOLETIM ESCOLAR", 
            font=("Arial", 20, "bold")
        )
        titulo.place(x=60, y=10)
        
        # Frame de seleções 
        frame_selecoes = ctk.CTkFrame(
            master=frame_conteudo, 
            fg_color="white",
            border_width=1,
            border_color="#e1e1e1",
            width=900,
            height=120,
            corner_radius=10
        )
        frame_selecoes.place(relx=0.15, rely=0.1, relwidth=0.5, relheight=0.1)
        
        # Campo Nome do Aluno 

        ctk.CTkLabel( master=frame_selecoes, text="NOME DO ALUNO:", font=("Arial", 14, "bold")).place(relx=0.03, rely=0.2)

        entry_nome = ctk.CTkEntry(
            master=frame_selecoes,
            width=300,
            height=35,
            font=("Arial", 12),
            placeholder_text="Digite o nome completo"
        )
        entry_nome.place(x=30, y=45)
        
        ctk.CTkLabel(master=frame_selecoes, text="CURSO:", font=("Arial", 14, "bold")).place(relx=0.37, rely=0.2)    
        selecao_ensino = ctk.CTkComboBox(
            master=frame_selecoes,
            values=cursos,
            font=("Arial", 12),
            width=180,
            state="readonly",
            dropdown_font=("Arial", 12)
        )
        selecao_ensino.place(x=350, y=45)
        selecao_ensino.set(cursos[0])

        ctk.CTkLabel(master=frame_selecoes, text="TURMA:", font=("Arial", 14, "bold")).place(relx=0.57, rely=0.2)
        selecao_turma = ctk.CTkComboBox(
            master=frame_selecoes,
            values=turmas,
            font=("Arial", 12),
            width=120,
            state="readonly"
        )
        selecao_turma.place(x=550, y=45)
        selecao_turma.set(turmas[0])

        ctk.CTkLabel(master=frame_selecoes, text="SÉRIE:", font=("Arial", 14, "bold")).place(relx=0.73, rely=0.2)
        selecao_serie = ctk.CTkComboBox(
            master=frame_selecoes,
            values=series,
            font=("Arial", 12),
            width=120,
            state="readonly"
        )
        selecao_serie.place(x=700, y=45)
        selecao_serie.set(series[0])

        # Frame da tabela 
        frame_tabela = ctk.CTkScrollableFrame(
            master=frame_conteudo,
            fg_color="white",
            border_width=1,
            border_color="#e1e1e1",
            width=900,
            height=450,
            corner_radius=10
        )
        frame_tabela.place(relx=0.15, rely=0.25)
        
        
        def criar_tabela():
            for widget in frame_tabela.winfo_children():
                widget.destroy()
            
            unidades = ["1º UNIDADE", "2º UNIDADE", "3º UNIDADE"]
            
            # Cabeçalho 
            for col, unidade in enumerate(unidades):
                header = ctk.CTkLabel(
                    master=frame_tabela,
                    text=unidade,
                    font=("Arial", 14, "bold"),
                    width=200,
                    height=40,
                    corner_radius=5,
                    fg_color=COLOR_SECONDARY,
                    text_color="white"
                )
                header.grid(row=0, column=col+1, padx=5, pady=5, sticky="nsew")
            
            # Matérias 
            for row, materia in enumerate(materias_atuais, start=1):
                bg_color = "#ecf0f1" if row % 2 == 0 else "#ffffff"
                
                # Nome da matéria
                lbl_materia = ctk.CTkLabel(
                    master=frame_tabela,
                    text=materia,
                    font=("Arial", 14),
                    width=180,
                    height=40,
                    corner_radius=5,
                    fg_color=bg_color,
                    anchor="w"
                )
                lbl_materia.grid(row=row, column=0, padx=5, pady=2, sticky="nsew")
                
                # Campos de nota
                for col in range(len(unidades)):
                    frame_nota = ctk.CTkFrame(
                        master=frame_tabela,
                        width=200,
                        height=40,
                        fg_color=bg_color,
                        corner_radius=5
                    )
                    frame_nota.grid(row=row, column=col+1, padx=5, pady=2, sticky="nsew")
                    
                    entry_nota = ctk.CTkEntry(
                        master=frame_nota,
                        width=180,
                        height=30,
                        font=("Arial", 12),
                        placeholder_text="0.0",
                        justify="center"
                    )
                    entry_nota.place(relx=0.5, rely=0.5, anchor="center")
        
        def mudar_ensino(escolha):
            nonlocal materias_atuais
            
            # Atualiza turmas 
            if escolha == "INTEGRAL":
                selecao_turma.configure(values=turmas_integral)
                selecao_turma.set(turmas_integral[0])
            else:
                selecao_turma.configure(values=turmas)
                selecao_turma.set(turmas[0])
            
            # Atualiza matérias 
            if escolha == "INFORMÁTICA":
                materias_atuais = materias_info
            elif escolha == "NUTRIÇÃO":
                materias_atuais = materias_nutri
            elif escolha == "ADMINISTRAÇÃO":
                materias_atuais = materias_adm
            elif escolha == "INTEGRAL":
                materias_atuais = materias_integral
            
            criar_tabela()

        selecao_ensino.configure(command=mudar_ensino)
        
        # Botões 
        btn_salvar = ctk.CTkButton(
            master=frame_conteudo,
            text="SALVAR BOLETIM",
            width=150,
            height=35,
            fg_color=COLOR_SECONDARY,
            hover_color=COLOR_HOVER,
            font=("Arial", 14, "bold"),
            corner_radius=8
        )
        btn_salvar.place(relx=0.45, rely=0.69)

        btn_imprimir = ctk.CTkButton(
            master=frame_conteudo,
            text="IMPRIMIR BOLETIM",
            width=150,
            height=35,
            fg_color=COLOR_SECONDARY,
            hover_color=COLOR_HOVER,
            font=("Arial", 14, "bold"),
            corner_radius=8
        )
        btn_imprimir.place(relx=0.53, rely=0.69)
        
        # Cria tabela inicial
        criar_tabela()
    
    def tela_registrar_cardapio():
        limparTela()
        ctk.CTkLabel(master=frame_conteudo, text="REGISTRAR CARDÁPIO", font=("Arial", 20,"bold")).place(x=60,y=10)


        # Frame para tabela 
        frame_tabela = ctk.CTkFrame(
            master=frame_conteudo,
            fg_color="white",
            border_width=1,
            border_color="#e1e1e1",
            width=920,
            height=500
        )
        frame_tabela.place(relx=0.15, rely=0.25)

        def criar_tabela():
            for widget in frame_tabela.winfo_children():
                widget.destroy()
            
            dias_semana = ["SEGUNDA-FEIRA", "TERÇA-FEIRA", "QUARTA-FEIRA","QUINTA-FEIRA","SEXTA-FEIRA"]
            horarios = ["CAFÉ", "MERENDA" ,"ALMOÇO", "MERENDA"]
            # Cabeçalho 
            for col, dia in enumerate(dias_semana):
                header = ctk.CTkLabel(
                    master=frame_tabela,
                    text=dia,
                    font=("Arial", 12, "bold"),
                    width=140,
                    height=40,
                    corner_radius=5,
                    fg_color=COLOR_SECONDARY,
                    text_color="white"
                )
                header.grid(row=0, column=col+1, padx=5, pady=10, sticky="nsew")
            
            # Linhas de horários
            for row, horario in enumerate(horarios, start=1):
                bg_color = "#ecf0f1" if row % 2 == 0 else "#ffffff"
                
                # Rótulo do horário
                lbl_horario = ctk.CTkLabel(
                    master=frame_tabela,
                    text=horario,
                    font=("Arial", 12),
                    width=150,
                    height=40,
                    corner_radius=5,
                    fg_color=bg_color,
                    anchor="w"
                )
                lbl_horario.grid(row=row, column=0, padx=5, pady=5, sticky="nsew")
                
                # Campos de entrada para cada dia
                for col in range(len(dias_semana)):
                    
                    entry = ctk.CTkEntry(
                        master=frame_tabela,
                        width=140,
                        height=35,
                        font=("Arial", 12),
                        justify="center",
                        fg_color=bg_color,
                        border_width=1,
                        border_color="#dddddd"
                    )
                    entry.grid(row=row, column=col+1, padx=5, pady=5, sticky="nsew")
                    
            
        criar_tabela()

        # Botão para salvar 
        btn_salvar = ctk.CTkButton(
            master=frame_conteudo,
            text="SALVAR HORÁRIOS",
            width=150,
            height=35,
            fg_color=COLOR_SECONDARY,
            hover_color=COLOR_HOVER,
            font=("Arial", 12, "bold"),
            corner_radius=8
        )
        btn_salvar.place(x=790, y=660)

    # Cabeçalho do menu
    label_titulo = ctk.CTkLabel(
        master=menu,
        text="SISTEMA ESCOLAR",
        font=("Arial", 20, "bold"),
        text_color="white"
    )
    label_titulo.place(x=25, y=40)

    # Botões do menu
    btn_style = {
        "master": menu,
        "width": 250,
        "height": 45,
        "corner_radius": 0,
        "border_width": 0,
        "font": ("Arial", 14),
        "fg_color": COLOR_PRIMARY,
        "hover_color": COLOR_HOVER,
        "text_color": "white"
    }

    #botão ver pedidos de documentos 
    btn_Solicitacoes = ctk.CTkButton(
        **btn_style,
        text="SOLICITAÇÕES",
        command=tela_documentos
    )
    btn_Solicitacoes.place(x=0, y=150)

    #botão registrar horarios
    btn_Horario = ctk.CTkButton(
        **btn_style,
        text="REGISTRAR HORÁRIOS",
        command=tela_registrar_horarios
    )
    btn_Horario.place(x=0, y=195)

    #botão registrar boletim 
    btn_registrar_boletim = ctk.CTkButton(
        **btn_style,
        text="REGISTRAR BOLETINS",
        command=tela_registrar_boletins
    )
    btn_registrar_boletim.place(x=0, y=240)

    #botão registrar cardapio
    btn_cardapio = ctk.CTkButton(
        **btn_style,
        text="REGISTRAR CARDÁPIO",
        command=tela_registrar_cardapio
    )
    btn_cardapio.place(x=0, y=285)


    # Botão de sair 
    btn5 = ctk.CTkButton(
        master=menu,
        text="SAIR",
        command=main_window.destroy,
        corner_radius=0,
        border_width=0,
        font=("Arial", 14),
        fg_color="#444444",
        hover_color=COLOR_ERROR,
        text_color="white"
    )

    btn5.place(relx=0, rely=0.92, relwidth=0.52, relheight=0.08)




    main_window.mainloop()

janela_login()