from tkinter import *

def bt_click():
    # Dexei de fazer a validação porque iria ter que refaturar muita coisa
    peso = float(ed_peso.get())
    altura = float(ed_altura.get())
    imc = peso / (altura * altura)
    lb_valor["text"] = "{:4.2f}".format(imc) # f"{imc:.2f}"
    if imc <= 18.4:
        lb_imc["text"] = "Abaixo do peso"
    elif imc > 18.4 and imc <= 24.9:
        lb_imc["text"] = "Normal"
    elif imc > 24.9 and imc <= 29.9:
        lb_imc["text"] = "Acima do peso"
    else:
        lb_imc["text"] = "Obeso"

i = Tk()
i.title("Calculadora de IMC")
i.geometry("800x600+250+30")
i.wm_iconbitmap("icone2.ico")


lb = Label(i,text="IMC = ")
lb.place(x=200,y=310)
lb_valor = Label(i,text="0")
lb_valor.place(x=230,y=310)

lb_peso = Label(i,text="Peso")
lb_peso.place(x=200,y=210)
ed_peso = Entry(i,width="25")
ed_peso.place(x=200,y=230)

lb_altura = Label(i,text="Altura")
lb_altura.place(x=200,y=260)
ed_altura = Entry(i,width="25")
ed_altura.place(x=200,y=280)

lb_imc = Label(i,text="")
lb_imc.place(x=280,y=310)

bt_imc = Button(i,width="20",text="Calcular IMC",command=bt_click)
bt_imc.place(x=200,y=340)

lb_eu  = Label(i,text="Gabriel Eduardo Schulze Machado")
lb_eu.place(x=200,y=400)

i.mainloop()