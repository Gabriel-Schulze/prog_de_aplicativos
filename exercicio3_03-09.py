import random

def menu():
    print("1 - Adição")
    print("2 - Subtração")
    escolha = int(input("Escolha numero 1 ou numero 2: "))

    if escolha == 1:
        soma()
    elif escolha == 2:
        subtracao()
    else:
        print("Opção Invalida!!")

def soma():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    print(num1," + ",num2," = ")
    resposta = int(input("Sua resposta: "))
    
    if resposta == (num1 + num2):
        print("Resposta Correta!")
    else:
        print("Resposta está incorreta!")

def subtracao():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    print(num1," - ",num2," = ")
    resposta = int(input("Sua resposta: "))
    
    if resposta == (num1 - num2):
        print("Resposta Correta!")
    else:
        print("Resposta está incorreta!")


menu()