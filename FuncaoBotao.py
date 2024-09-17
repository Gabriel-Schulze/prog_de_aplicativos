# ------- BOTÃO COM FUNÇÃO
# ------- ALUNO GABRIEL EDUARDO SCHULZE MACHADO

from tkinter import *

# CRIANDO UMA FUNÇÃO PARA CLIQUE NI BOTÃO
def bt_click():
    # O label QUE USA PROPRIEDADE text RECEBERA A MENSAGEM "trocou o texto"
    lb['text'] = "Trocou o texto"
    # ESSE print EXIBE O TEXTO NA TELA DO CONSOLE
    print("O botão foi clicado")

def bt_clickar():
    # ESSE print EXIBE O TEXTO DIGITADO NA CAIXA DE TEXTO
    # EXIBE NA label DA TELA
    print(ed.get())
    lb['text'] = ed.get

i = Tk()

i.title("Programa Financeiro")
i.geometry('980x720+230+30')

i["bg"] = "brown"
i.wm_iconbitmap('icone.ico')

lb = Label(i, text="Nome do Usuario")
lb.place(x=100,y=100)

bt = Button(i, width='20',text="OK",command=bt_click)
bt.place(x=230,y=100)

# CRIA UM botao E POSIONA ABAIXO DO BOTAO ok
bt = Button(i, width='20',text="OK",command=bt_click)
bt.place(x=230,y=100)

ed = Entry(i)
ed.place(x=230,y=150)

lb_nome = Label(i,width='39',text='Gabriel Eduardo Schulze Machado')
lb_nome.place(x=100,y=200)

i.mainloop()