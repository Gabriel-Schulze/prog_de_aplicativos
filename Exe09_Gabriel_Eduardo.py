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

# O CODIGO ABAIXO POSICIONA CADA label EM LUGARES DIFERENTES

#lb1.pack(side=TOP,fill=X) # O PARAMETRO fill É RESPONSAVEL DO PREENCIMENTO 100%, DEVE USAR X PARA HORIZONTAL E Y PARA VERTICAL
# lb2.pack(side=RIGHT, fill=Y)
# lb3.pack(side=LEFT,fill=Y)
# lb4.pack(side=BOTTOM,fill=X)

# lb2.pack(side=RIGHT, fill=Y)
# lb3.pack(side=LEFT,fill=Y)
# lb1.pack(side=TOP,fill=BOTH)
# lb4.pack(side=BOTTOM,fill=BOTH)

lb1.pack(side=TOP,fill=BOTH, expand=1)
lb4.pack(side=TOP,fill=BOTH,expand=1)
lb2.pack(side=TOP,fill=BOTH,expand=1)
lb3.pack(side=TOP,fill=BOTH,expand=1)



i.mainloop()