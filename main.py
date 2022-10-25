from tkinter import *
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

        bot_return = Button(frame1, image=img_voltar, command=self.tela_inicial)
        bot_return.place(width=150, height=50, x=564, y=221)
        self.master.mainloop()

    def tela_tecnico(self):
        frame1 = Frame(self.master)
        frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        #carregamento das iagens:
        img_fundo = PhotoImage(file="imagens\\tela_tecnicos.png")
        img_voltar = PhotoImage(file="imagens\\bot_return.png")


        lab_fundo = Label(frame1, image=img_fundo)
        lab_fundo.pack()

        bot_return = Button(frame1, image=img_voltar, command=self.tela_inicial)
        bot_return.place(width=150, height=50, x=564, y=221)
        self.master.mainloop()




Aplication()