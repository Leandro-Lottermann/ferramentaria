from tkinter import *
import posiciona




master = Tk()
master.bind('<Button-1>', posiciona.inicio_place)
master.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg, master))
master.bind('<Button-2>', lambda arg: posiciona.para_geometry(master))

master.geometry("800x600")
master.resizable(False, False)






#Archives Imports:
img_fundo = PhotoImage(file="imagens\\Ferramentaria.png")
img_bot_ferramenta = PhotoImage(file="imagens\\bot_ferramenta.png")
img_bot_tecnico = PhotoImage(file="imagens\\bot_tecnico.png")
lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()

bot_tecnico = Button(master, image=img_bot_tecnico, bd=2)
bot_tecnico.place(width=166, height=166, x=273, y=380)

bot_ferramenta = Button(master, image=img_bot_ferramenta, bd=2)
bot_ferramenta.place(width=166, height=166, x=557, y=380)






master.mainloop()
