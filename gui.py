from tkinter import *
from tkinter import ttk
import posiciona
from funcional import *
from tkinter import messagebox


class Validacao:
    def validanumero(self, entrada):
        if entrada == "": return True
        try:
            value = int(entrada)
        except ValueError:
            return False
        return 0 <= value


class Aplication(Validacao):
    def __init__(self):
        self.bancotecnicos = DBtecnicos()
        self.master = Tk()
        self.master.bind('<Button-1>', posiciona.inicio_place)
        self.master.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, self.master))
        self.master.bind('<Button-2>', lambda arg: posiciona.para_geometry(self.master))
        self.valida_entrada_int()
        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.tela_inicial()

    def valida_entrada_int(self):
        self.validacaonumerica = (self.master.register(self.validanumero), "%P")

    def tela_inicial(self):
        #Archives Imports:
        frame1 = Frame(self.master)
        frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        #Carregando imagens:
        img_fundo = PhotoImage(file="imagens\\tela_inicial.png")
        img_bot_ferramenta = PhotoImage(file="imagens\\bot_ferramenta.png")
        img_bot_tecnico = PhotoImage(file="imagens\\bot_tecnico.png")
        img_bot_reserva = PhotoImage(file="imagens\\bot_reserva.png")
        lab_fundo = Label(frame1, image=img_fundo)
        lab_fundo.pack()

        bot_tecnico = Button(frame1, image=img_bot_tecnico, bd=2, command=self.tela_tecnico)
        bot_tecnico.place(width=167, height=167, x=201, y=381)

        bot_ferramenta = Button(frame1, image=img_bot_ferramenta, bd=2, command=self.tela_ferramenta)
        bot_ferramenta.place(width=167, height=167, x=400, y=381)

        bot_reserva = Button(frame1, image=img_bot_reserva)
        bot_reserva.place(width=167, height=167, x=597, y=381)

        self.master.mainloop()

    def tela_ferramenta(self):
        self.bacoferramentas = DBferramentas()
        frame1 = Frame(self.master)
        frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        #carregamento das imagens:
        img_fundo = PhotoImage(file="imagens\\tela_ferramentas.png")
        img_voltar = PhotoImage(file="imagens\\bot_return.png")
        img_add = PhotoImage(file="imagens\\bot_add.png")
        img_del = PhotoImage(file="imagens\\bot_excluir.png")

        lab_fundo = Label(frame1, image=img_fundo)
        lab_fundo.pack()

        #Entry
        ent_descricao = Entry(frame1)
        ent_fabricante = Entry(frame1)
        ent_part_nunber = Entry(frame1, validate="key", validatecommand=self.validacaonumerica)
        ent_tamanho = Entry(frame1, validate="key", validatecommand=self.validacaonumerica)
        ent_tipo = Entry(frame1)
        ent_material = Entry(frame1)
        ent_reserva_max = Entry(frame1, validate="key", validatecommand=self.validacaonumerica)

        ent_descricao.place(width=494, height=22, x=135, y=86)
        ent_fabricante.place(width=211, height=22, x=134, y=119)
        ent_part_nunber.place(width=148, height=22, x=480, y=119)
        ent_tamanho.place(width=70, height=22, x=135, y=152)
        ent_tipo.place(width=298, height=22, x=480, y=152)
        ent_material.place(width=298, height=22, x=135, y=185)
        ent_reserva_max.place(width=52, height=22, x=591, y=186)

        #ComboBox:
        lista_voltagens = [110, 220, "n/a"]
        lista_un_medida = ["cm", "m", "mm", "pol"]
        cb_un_medida = ttk.Combobox(frame1, values=lista_un_medida)
        cb_un_medida.place(width=40, height=22, x=213, y=152)
        cb_voltagem = ttk.Combobox(frame1, values=lista_voltagens)
        cb_voltagem.place(width=71, height=22, x=348, y=152)

        # treeview:
        tv = ttk.Treeview(frame1, columns=("ferramenta", "fabricante", "pnumber", "tamanho", "unm", "voltagem", "tipo", "material", "resmax"), show="headings")

        tv.column("ferramenta", minwidth=0, width=60)
        tv.column("fabricante", minwidth=0, width=80)
        tv.column("pnumber", minwidth=0, width=50)
        tv.column("tamanho", minwidth=0, width=25)
        tv.column("unm", minwidth=0, width=25)
        tv.column("voltagem", minwidth=0, width=25)
        tv.column("tipo", minwidth=0, width=25)
        tv.column("material", minwidth=0, width=25)
        tv.column("resmax", minwidth=0, width=25)

        tv.heading("ferramenta", text = "Ferramenta")
        tv.heading("fabricante",text =  "Fab.")
        tv.heading("pnumber", text = "Pn")
        tv.heading("tamanho", text = "Tam")
        tv.heading("unm", text = "UnM")
        tv.heading("voltagem", text= "Vol.")
        tv.heading("tipo", text= "Tipo")
        tv.heading("material", text= "Mat.")
        tv.heading("resmax", text= "ResMax")
        self.inserta_dados_ferramenta_tv(tv)
        tv.place(width=751, height=293, x=24, y=280)

        #botoes:
        bot_add = Button(frame1, image=img_add, command=lambda: self.add_feramenta(ent_descricao.get(), ent_fabricante.get(), ent_part_nunber.get(), ent_tamanho.get(), cb_voltagem.get(), cb_voltagem.get(), ent_tipo.get(), ent_material.get(), ent_reserva_max.get()))
        bot_add.place(width=50, height=50, x=134, y=221)
        bot_del = Button(frame1, image=img_del, command=lambda: self.del_item(tv.item(tv.selection()[0], "values")))

        bot_del.place(width=50, height=50, x=202, y=221)

        bot_return = Button(frame1, image=img_voltar, command=self.tela_inicial)
        bot_return.place(width=150, height=50, x=564, y=221)

        self.master.mainloop()

    def tela_tecnico(self):
        self.bancotecnicos = DBtecnicos()
        frame1 = Frame(self.master)
        frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        #carregamento das iagens:
        img_fundo = PhotoImage(file="imagens\\tela_tecnicos.png")
        img_voltar = PhotoImage(file="imagens\\bot_return.png")
        img_add = PhotoImage(file="imagens\\bot_add.png")
        img_del = PhotoImage(file="imagens\\bot_excluir.png")

        lab_fundo = Label(frame1, image=img_fundo)
        lab_fundo.pack()

        #Entry:
        ent_nome = Entry(frame1)
        ent_cpf = Entry(frame1, validate="key", validatecommand=self.validacaonumerica)
        ent_tel = Entry(frame1, validate="key", validatecommand=self.validacaonumerica)
        ent_equipe = Entry(frame1)

        ent_nome.place(width=441, height=22, x=184, y=87)
        ent_cpf.place(width=269, height=22, x=184, y=118)
        ent_tel.place(width=269, height=23, x=184, y=150)
        ent_equipe.place(width=168, height=21, x=455, y=185)

        #ComboBox:
        lista_turnos = ["MANHÃ", "TARDE", "NOITE"]
        cb_turnos = ttk.Combobox(frame1, values=lista_turnos)
        cb_turnos.place(width=148, height=22, x=184, y=185)

        #treeview:
        tv = ttk.Treeview(frame1, columns= ("cpf", "nome", "telefone", "turno", "equipe"), show= "headings")

        tv.column("cpf", minwidth=0, width=60)
        tv.column("nome", minwidth=0, width=80)
        tv.column("telefone", minwidth=0, width=50)
        tv.column("turno", minwidth=0, width=25)
        tv.column("equipe", minwidth=0, width=25)

        tv.heading("cpf", text="CPF")
        tv.heading("nome", text="TÉCNICO")
        tv.heading("telefone", text="CONTATO")
        tv.heading("turno", text="TURNO")
        tv.heading("equipe", text="EQUIPE")
        self.inserta_dados_tecnico_tv(tv)
        tv.place(width=751, height=293, x=24, y=280)

        #botoes:
        bot_add = Button(frame1, image=img_add, command= lambda: self.add_tecnico(ent_cpf.get(), ent_nome.get(), ent_tel.get(), cb_turnos.get(), ent_equipe.get()))
        bot_add.place(width=50, height=50, x=134, y=221)
        bot_del = Button(frame1, image=img_del, command= lambda : self.del_item(tv.item(tv.selection()[0], "values"), "t")) #sem o 0 retorna uma string do indice no tv
        bot_del.place(width=50, height=50, x=202, y=221)

        bot_return = Button(frame1, image=img_voltar, command=self.tela_inicial)
        bot_return.place(width=150, height=50, x=564, y=221)



        self.master.mainloop()

    def tela_reserva(self):
        frame1 = Frame(self.master)
        frame1.place(relx=0, rely=0, relwidth=1, relheight=1)

    def add_tecnico(self,cpf, nome, telefone, turno, equipe):
        if cpf == "" or nome == "" or telefone == "" or turno == "" or equipe == "":
            messagebox.showerror("ERRO", "Não foi possível adicionar!")
        else:
            listadados = (cpf, nome, telefone, turno, equipe)
            self.bancotecnicos.add_novo_tec(listadados)

            self.tela_tecnico()

    def inserta_dados_tecnico_tv(self, tv):
        for (cpf, nome, telefone, turno, equipe) in self.bancotecnicos.linhas: #Cada elemento já um item da lista, aqui estou separando as colunas
            tv.insert("", "end", values= (cpf, nome, telefone, turno, equipe))

    def del_item(self, selecionado, tipo="f"):
        try:
            if tipo == "t":
                self.bancotecnicos.remove_tec(int(selecionado[0]))

                self.tela_tecnico()
            else:
                self.bacoferramentas.remove_fer(int(selecionado[2]))
                self.tela_ferramenta()
        except:
            messagebox.showerror("ERRO", "Não foi possivel excluir")
    def add_feramenta(self, ferramenta, fabricante, pnumber, tamanho, unm, voltagem, tipo, material, resmax):
        if ferramenta == "" or fabricante == "" or pnumber == "" or tamanho == "" or unm == "" or voltagem == "" or tipo == "" or material == "" or resmax == "":
            messagebox.showerror("ERRO", "Não foi possível adicionar!")
        else:
            listadados = (ferramenta, fabricante, int(pnumber), float(tamanho), unm, voltagem, tipo, material, int(resmax))
            self.bacoferramentas.add_nova_fer(listadados)

            self.tela_ferramenta()

    def inserta_dados_ferramenta_tv(self, tv):
        for (ferramenta, fabricante, pnumber, tamanho, unm, voltagem, tipo, material, resmax) in self.bacoferramentas.linhas:
            tv.insert("", "end", values = (ferramenta, fabricante, pnumber, tamanho, unm, voltagem, tipo, material, resmax))

    def alertaErro(self):
        messagebox.showerror("ERRO", "Não foi possivel excluir")