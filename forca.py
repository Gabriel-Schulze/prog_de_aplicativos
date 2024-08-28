#A CLASSE random É RESPONSAVEL POR SORTEAR AS PALAVRAS DO JOGO
import random

#a variavel do tipo ARRAY que ira amarzenar os simbolos para a forca e colocar nas posicoes INDICES
FORCAIMF = ['''
 +---+
 |   |
     |
     |
     |
     |
========= ''','''
 +---+
 |   |
 O   |
     |
     |
     |
========= ''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
========= ''','''
 +---+
 |   |
 O   |
/|   |
     |
     |
========= ''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
========= ''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========= ''','''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========= ''']

#VARIAVEL ABAIXO IRA ARMAZENAR AS PALAVRAS QUE FOREM PROGRAMADAS E .split É RESPONSAVEL DE ACESSAR OS CARACTERES
palavra = 'banana telescopio cachorro martelo girafa hamburguer tio pai carro gabrielmachado'.split()

#FUNCAO PRINCIPAL DO PROGRAMA
def main():
    #VARIAVEL DEVE SER GLOBAL PORQUE FOR DECLARADA FORA DA FUNCAO
    global FORCAIMF
    #APENAS ÁRA EXIBIR UM CABECALHO DO JOGO
    print("F o R C A")
    #DECLARAR AS VARIAVEIS PARA COMECAREM VAZIAS
    letrasErradas = ""
    letrasAcertadas = ""
    #BUSCA A FUNCAO geraPalavraAleatoria E CRIA EM LETRAS MAIUSCULAS upper
    palavraSecreta = geraPalavraAleatoria().upper()
    #RESPONSAVEL DE INICIALIZAR O JOGO
    jogando = True

    #ENQUANTO ELE ESTIVER JOGANDO, SERA IMPRESSO AS LETRAS ERRADAS, ACERTADAS
    while jogando:
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)
        #VARIAVEL VAI RECEBER AS LETRAS ERRADAS E AS CERTAS E A FUNCAO recebePalpite EXECUTOU
        palpite = recebePalpite(letrasErradas + letrasAcertadas)
        #SE O palpite EXISTIR NA palavraSecreta INCREMENTAR MAIS UM NO palpite E ARMAZENAR A LETRA NA VARIAVEL letrasAcertadas
        if palpite in palavraSecreta:
            letrasAcertadas += palpite
            if VerificaSeGanhou(palavraSecreta, letrasAcertadas):
                print("Exato! A palavra secreta é: " + palavraSecreta + " você ganhou!")
                jogando = False
        else:
            letrasErradas += palpite
            #CODIGO ABAIXO LIMITA A QUANTIDADE DE TENTATIVAS CONFORME A QTDE DE SEU ARRAY forcaimg(5)
            if len(letrasErradas) == len(FORCAIMF) - 1:
                imprimeJogo(letrasErradas,letrasAcertadas, palavraSecreta)
                print("Você excedeu o seu limite de palpites!")
                print("Depois de " + str(len(letrasErradas)) + " letras erradas e " + str(len(letrasAcertadas)),end="")
                print("letras corretas, a palavra era: " + palavraSecreta + ".")
                jogando = False
        if not jogando:
            if JogarNovamente():
                letrasErradas = ""
                letrasAcertadas = ""
                jogando = True
                palavraSecreta = geraPalavraAleatoria().upper()

# FUNCAO QIE RETORNA UMA STRING A PARTIR DA LISTA DE PALAVRAS GLOBAL
def geraPalavraAleatoria():
    global palavras
    return random.choice(palavras)

# FUNCAO RECEBE UMA STRING PALAVRA OU LISTA IMPRIME ESSTA LISTA COM A QUANTIDADE DE ESPAÇOS ENTRE AS LETRA OU STRING
def imprimeComEspacos(palavra):
    for letra in palavra:
        print(letra, end="")
    # DEVE FICAR FORA DO LAÇO for
    print()

# FEITO A PARTIR DA VARIAVEL global QUE CONTEM AS IMAGENS DO JOGO EM ascii art, E TAMBEM AS LETRAS CHUTADAS DE MANERA CORRETA E AS LETRAS ERRADAS E A PALAVRA SECRETA
def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    #VARIAVEL DEVE SER GLOBAL PORUQE FOI DECLARADA FORA DA FUNCAO
    global FORCAIMF
    #VAI IMPRIMIR O ARRAY DE LETRAS ERRADAS E VERIFICA O TAMANHO (busca a posicao) DA FIGURA
    print(FORCAIMF[len(letrasErradas)]+"\n")
    print("Letras Erradas: ",end="")
    imprimeComEspacos(letrasErradas)

    #VARIAVEL IMPRIME O CARACTER menos PARA VIZUALIZAR A QTDE DE CARACTERES DA PALAVRA SECRETA
    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]

#FUNCAO FEITA PARA GARANTIR QUE O USUARIO COLOQUE UMA ENTRADA VALIDA OU SEJA UNICA LETRA QUE ELE AINDA NÃO TENHA CHUTADO
def recebePalpite(palpitesFeitos):
    while True:
        #COLA UM ESPAÇO ENTRE A MENSAGEM
        print()
        palpite = input("Adivinhe uma letra. \n").upper()
        # SE USUARIO DIGITAR MAIS DE UMA LETRA
        if len(palpite) != 1:
            print("Coloque uma unica letra.")
        #SE A LETRA JA TIVER SIDO DIGITADA NA LISTA
        elif palpite in palpitesFeitos:
            print("Essa letra ja existe, digite outra. \n")
        #SE ELE NÃO DIGITAR UMA LETRA OU NUMERO
        elif not 

