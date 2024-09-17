# ------- PRIMEIRA TELA WIDGET
# ------- ALUNO GABRIEL EDUARDO SCHULZE MACHADO

# O COMANDO ABAIXO IMPORTA TUDO DA BIBLIOTECA QUE É NECESSARIO
# PARA A CRIAÇÃO DE TELAS
from tkinter import *

# i (INSTANCIAR) RECEBE O OBJETO tk
i = Tk()

# O CODIGO ABAIXO GERA O TITULO DA JANELA
i.title('Programa Financeiro')

# PROPRIEDADE QUE ALTERA O TAMANHO DA JANELA (980X720) E DISTANCIA DA DIREITA E TOPO DA TELA (250X30)
i.geometry('720x480+250+30')

# PROPRIEDADES GRAFICAS, COR DE FUNDO DA TELA (bg) ou (background)
# NÃO PODE PODE PASAR O i COM .
i["bg"] = "brown"

# CRIA O ICONE NA JANELA, VOCÊ DEVE TER A IMAGEM NO MESMO LOCAL DO CODIGO
i.wm_iconbitmap('icone.ico')

lb = Label(i,text='Nome do Usuario')
lb.place(x=100,y=100)

# CRIA UM BOTAO E POSICIONA (place) ELE EM RELAÇÃO A LABEL
bt = Button(i,width='20', text='OK')
bt.place(x=230,y=100)

lb_nome = Label(i,width='39',text='Gabriel Eduardo Schulze Machado')
lb_nome.place(x=100,y=200)

# GERA A JANELA GRAFICA
i.mainloop()
