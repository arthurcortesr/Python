import random

def jogar():
    
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1,101)

    total_de_tentativas = 1

    pontos = 1000

    print("Qual o nível de dificuldade?")
    nivel = int(input("(1)Fácil - (2)Médio - (3)Difícil: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um numero entre 1 e 100: "))
        print("Você digitou:", chute)

        acertou = numero_secreto == chute
        menor = numero_secreto > chute
        maior = numero_secreto < chute
    
        if chute < 1 or chute > 100:
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        if acertou:
            print("\nVocê acertou e fez {} pontos".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O numero secreto é menor que o numero do chute")
            elif menor:
                print("Você errou! O numero secreto é maior que o numero do chute")
            pontos_perdidos = round(abs(numero_secreto - chute) / 3)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")
    print("O numero secreto era: {}".format(numero_secreto))

if __name__ == "__main__":
    jogar()