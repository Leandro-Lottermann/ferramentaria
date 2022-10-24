from tkinter import *

def clicou(label):
    label["text"] = "clicou"

def menuinicial():
    janela = Tk()
    janela.minsize(550,400)
    janela.maxsize(550, 400)
    janela.title("FERRAMENTARIA")

    titulo = Label(janela, text="Escolha uma opção:", font="Arial 16")
    titulo.place(relx=0.02, rely=0.05)
    imagem = PhotoImage(file="ferramentas.png")

    button_ferramenta = Button(janela, image=imagem, command=lambda: clicou(titulo))

    button_ferramenta.pack()

    janela.mainloop()


menuinicial()