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


# PARAMETRO anchor POSICIONA O OBJETO PASSANDO A DIRECAO E COORDENADAS
# lb1.pack(side=LEFT)
# lb2.pack(side="left")
# lb3.pack(anchor="w")
# lb4.pack(anchor="w")

# lb1.pack(side=LEFT)
# lb2.pack(side="left")
# lb3.pack(anchor="w")
# lb4.pack(side=BOTTOM,anchor="sw")

# lb1.pack(side=LEFT)
# lb2.pack(side="left")
# lb3.pack(anchor="w")
# lb4.pack(anchor="e")

# lb1.pack(side=LEFT)
# lb2.pack(side="left")
# lb3.pack(anchor="w")
# lb4.pack(side=BOTTOM,anchor="e")

lb1.pack(side=LEFT)
lb2.pack(side="left")
lb3.pack(anchor="w")
lb4.pack(side=BOTTOM,anchor=CENTER)


i.mainloop()