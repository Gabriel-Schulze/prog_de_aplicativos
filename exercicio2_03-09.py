import random

def gera_num_aleatorio():
    numBaixo = int(input("Insira um numero baixo: "))
    numAlto = int(input("Insira um numero alto: "))
    return random.randint(numBaixo,numAlto)

def get_chute():
    return int(input("O numero que estou pensando é: "))

def verifica_chute(num_secreto,chute):
    acertou = False
    while not acertou:
        if num_secreto == chute:
            print("Parabéns, você acertou!")
            acertou = True
        elif chute < num_secreto:
            chute = int(input("Palpite muito baixo, tente novamente!: "))
        else:
            chute = int(input("Palpite muito alto, tente novamente!: "))

def main():
    num_secreto = gera_num_aleatorio()
    chute = get_chute()
    verifica_chute(num_secreto,chute)

main()
