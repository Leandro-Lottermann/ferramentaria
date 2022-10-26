from tkinter import *
from tkinter import ttk
import posiciona


class Aplication():
    def __init__(self):
        self.master = Tk()
        self.master.bind('<Button-1>', posiciona.inicio_place)
        self.master.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, self.master))
        self.master.bind('<Button-2>', lambda arg: posiciona.para_geometry(self.master))

        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.tela_inicial()

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
        frame1 = Frame(self.master)
        frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        #carregamento das iagens:
        img_fundo = PhotoImage(file="imagens\\tela_ferramentas.png")
        img_voltar = PhotoImage(file="imagens\\bot_return.png")
        img_add = PhotoImage(file="imagens\\bot_add.png")
        img_del = PhotoImage(file="imagens\\bot_excluir.png")

        lab_fundo = Label(frame1, image=img_fundo)
        lab_fundo.pack()

        #Entry
        entry_descricao = Entry(frame1)
        entry_fabricante = Entry(frame1)
        entry_part_nunber = Entry(frame1)
        entry_tamanho = Entry(frame1)
        entry_tipo = Entry(frame1)
        entry_material = Entry(frame1)
        entry_reserva_max = Entry(frame1)

        entry_descricao.place(width=494, height=22, x=135, y=86)
        entry_fabricante.place(width=211, height=22, x=134, y=119)
        entry_part_nunber.place(width=148, height=22, x=480, y=119)
        entry_tamanho.place(width=70, height=22, x=135, y=152)
        entry_tipo.place(width=298, height=22, x=480, y=152)
        entry_material.place(width=298, height=22, x=135, y=185)
        entry_reserva_max.place(width=52, height=22, x=591, y=186)

        #ComboBox:
        lista_voltagens = [110, 220]
        cb_voltagem = ttk.Combobox(frame1, values=lista_voltagens)
        cb_voltagem.place(width=71, height=22, x=348, y=152)

        #botoes:
        bot_add = Button(frame1, image=img_add)
        bot_add.place(width=50, height=50, x=134, y=221)
        bot_del = Button(frame1, image=img_del)
        bot_del.place(width=50, height=50, x=202, y=221)

        bot_return = Button(frame1, image=img_voltar, command=self.tela_inicial)
        bot_return.place(width=150, height=50, x=564, y=221)

        self.master.mainloop()

    def tela_tecnico(self):
        frame1 = Frame(self.master)
        frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        #carregamento das iagens:
        img_fundo = PhotoImage(file="imagens\\tela_tecnicos.png")
        img_voltar = PhotoImage(file="imagens\\bot_return.png")
        img_add = PhotoImage(file="imagens\\bot_add.png")
        img_del = PhotoImage(file="imagens\\bot_excluir.png")

        lab_fundo = Label(frame1, image=img_fundo)
        lab_fundo.pack()

        #botoes:
        bot_add = Button(frame1, image=img_add)
        bot_add.place(width=50, height=50, x=134, y=221)
        bot_del = Button(frame1, image=img_del)
        bot_del.place(width=50, height=50, x=202, y=221)

        bot_return = Button(frame1, image=img_voltar, command=self.tela_inicial)
        bot_return.place(width=150, height=50, x=564, y=221)
        self.master.mainloop()



