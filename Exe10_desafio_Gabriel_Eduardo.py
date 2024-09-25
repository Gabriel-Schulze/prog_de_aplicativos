from tkinter import *

i = Tk()

i.title("Programa Financeiro")
i.geometry("800x600+250+30")
i.wm_iconbitmap("icone.ico")

lbnada1 = Label(i,width=40,height=15)
lbnada1.grid(row=1,column=1)

lb1 = Label(i,text="LOGIN",bg="yellow")
# O COMPONENTE .grid SERVE TAMBEM PARA POSICIONAR UTILIZANDO INDICATIVO DE LINHA (row) E COLUNA (column)
lb1.grid(row=2,column=2)

ed1 = Entry(i)
ed1.grid(row=2,column=3)

lbnada2 = Label(i)
lbnada2.grid(row=3,column=1)

lb2 = Label(i,text="SENHA",bg="red")
lb2.grid(row=4,column=2)

ed2 = Entry(i)
ed2.grid(row=4,column=3)

lbnada3 = Label(i)
lbnada3.grid(row=5,column=1)

bt1 = Button(i,text="Login")
bt1.grid(row=6,column=3)


i.mainloop()