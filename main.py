from tkinter import *

def cmd_ferramentas():
    jan_ferramentaria = Tk()
    jan_ferramentaria.minsize(550, 400)
    jan_ferramentaria.maxsize(550, 400)
    texto = Label(jan_ferramentaria, text="FERRAMENTAS", font="Arial 20")
    texto.pack()
    jan_ferramentaria.mainloop()
def cmd_tecnicos():
    jan_tecnicos = Tk()
    jan_tecnicos.minsize(550, 400)
    jan_tecnicos.maxsize(550, 400)
    texto = Label(jan_tecnicos, text="TECNICOS", font="Arial 20")
    texto.pack()
    jan_tecnicos.mainloop()

def menuinicial():
    m_window = Tk()
    m_window.minsize(550, 400)
    m_window.maxsize(550, 400)
    m_window.title("FERRAMENTARIA - Menu Principal   v.1")

    #TEXTOS:
    text_titulo = Label(m_window, text="FERRAMENTARIA", font="Arial 18", borderwidth=2, relief="solid", pady=5, padx=5)
    text_titulo.grid(row=1, column=1, columnspan=2, padx=8, pady=5)
    text_selecione = Label(m_window, text="Escolha sua Opção:", font="Arial 14")
    text_selecione.grid(row=2, column=0, pady=40,rowspan=2)
    text_tecnicos = Label(m_window, text="Técnicos")
    text_tecnicos.grid(row=6, column=1)
    text_ferramentas = Label(m_window, text="Ferramentas")
    text_ferramentas.grid(row=6,column=2)

    #botões:
    img_fer = PhotoImage(file="ferramentas.png")
    img_tec = PhotoImage(file= "tecnico.png")

    b_ferramentas = Button(m_window, image=img_fer, command=cmd_ferramentas)
    b_tecnicos = Button(m_window, image=img_tec, command=cmd_tecnicos)
    b_tecnicos.grid(row=5,column=1)
    b_ferramentas.grid(row=5, column=2)




    m_window.mainloop()

menuinicial()