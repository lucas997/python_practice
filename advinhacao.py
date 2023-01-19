import random

def jogar():

    print('*******************************')
    print('Bem vindo ao jogo da advinhação')
    print('*******************************')

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina a dificuldade: '))

    if nivel == 1:
        tentativas = 20   
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5
        
        
    for rodada in range(1, tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, tentativas))
        chute_str = input('Digite um número entre 1 e 100: ')
        
        chute = int(chute_str)
        
        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100: ')
            continue

        acertou = chute == numero_secreto
        is_maior = chute > numero_secreto
        is_menor = chute < numero_secreto
        
        if(acertou):
            print('você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if(is_maior):
                print('você errou! O seu chute é maior do que o número secreto.')
            elif(is_menor):
                print('você errou! O seu chute é menor do que o número secreto.')

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        
print('Fim do jogo!')