from tkinter import *

i = Tk()

i.title("Programa Financeiro")
i.geometry("800x600+250+30")
i.wm_iconbitmap("icone.ico")

lb1 = Label(i, text="Label 1", bg="yellow")
lb1.place(x=230,y=200)

lb2 = Label(i, text="Label 2", bg="red")
lb2.place(x=230,y=200)

lb3 = Label(i, text="Label 3", bg="pink")
lb3.place(x=230,y=200)

lb4 = Label(i, text="Label 4", bg="green")
lb4.place(x=230,y=200)

# A FUNCAO pack POSICIONA O MEU OBJETO NA PARTE SUPERIOR(PADRAO) E SEGUE A ORDEM QUE EU DECLAREI
# lb1.pack()
# lb2.pack()
# lb3.pack()
# lb4.pack()

# PARAMETRO side DEFINE A POSICAO DO OBJETO PASSANDO "top","left","right" ou "bottom"
# lb1.pack(side="top")
# lb2.pack(side="left")
# lb3.pack(side="right")
# lb4.pack(side="bottom")

# lb1.pack(side="left")
# lb2.pack(side="left")
# lb3.pack()
# lb4.pack()

i.mainloop()