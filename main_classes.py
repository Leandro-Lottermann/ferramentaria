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
        img_fundo = PhotoImage(file="imagens\\Ferramentaria.png")
        img_bot_ferramenta = PhotoImage(file="imagens\\bot_ferramenta.png")
        img_bot_tecnico = PhotoImage(file="imagens\\bot_tecnico.png")
        lab_fundo = Label(frame1, image=img_fundo)
        lab_fundo.pack()

        bot_tecnico = Button(frame1, image=img_bot_tecnico, bd=2)
        bot_tecnico.place(width=166, height=166, x=273, y=380)

        bot_ferramenta = Button(frame1, image=img_bot_ferramenta, bd=2, command=self.tela_ferramenta)
        bot_ferramenta.place(width=166, height=166, x=557, y=380)
        self.master.mainloop()
    def tela_ferramenta(self):
        frame1 = Frame(self.master)
        frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        img_fundo = PhotoImage(file="imagens\\ferramenta.png")
        lab_fundo = Label(frame1, image=img_fundo)
        lab_fundo.pack()

        self.master.mainloop()






Aplication()