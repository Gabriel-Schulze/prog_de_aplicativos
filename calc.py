from tkinter import *

def bt_click_soma():
    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric():
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 + num2
        lb["bg"] = "#00fa9a"
    else:
        lb["text"] = "Valores são invalidos"
        lb["bg"] = "red"

def bt_click_subtracao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 - num2

def bt_click_multiplicacao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 * num2

def bt_click_divisao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 / num2

i = Tk()
i.title("Programa Financeiro")
i.geometry("800x600+250+30")
i.wm_iconbitmap("icone.ico")

lb = Label(i,text="0")
lb.place(x=230,y=200)

bt_soma = Button(i, width="5",text="+",command=bt_click_soma)
bt_soma.place(x=230,y=230)

bt_subtracao = Button(i, width="5",text="-",command=bt_click_subtracao)
bt_subtracao.place(x=280,y=230)

bt_multiplicacao = Button(i, width="5",text="*",command=bt_click_multiplicacao)
bt_multiplicacao.place(x=330,y=230)

bt_divisao = Button(i, width="5",text="/",command=bt_click_divisao)
bt_divisao.place(x=380,y=230)

ed1 = Entry(i,width="32")
ed1.place(x=230,y=150)

ed2 = Entry(i,width="32")
ed2.place(x=230,y=180)

lb_eu  = Label(i,text="Gabriel Eduardo Schulze Machado")
lb_eu.place(x=230,y=290)

i.mainloop()