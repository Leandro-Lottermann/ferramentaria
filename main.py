from tkinter import *

def cadastroTecnico():
    janela = Tk()
    janela.minsize(500,350)

    imagem = PhotoImage(file="ferramentas.png")

    button_ferramenta = Button(janela, image=imagem)

    button_ferramenta.pack(pady=20)

    janela.mainloop()
cadastroTecnico()