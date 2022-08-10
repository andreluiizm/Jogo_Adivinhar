from random import randint

#Coleta informações do usuário e nível de jogo
print('ADIVINHE O NUMERO!!\n')
nome = input('Qual o seu nome? ')
print(f'\nOlá {nome}, Vamos começar?\n')
nivel= int(input('Existem 3 tipos de níveis:\nNivel 1: 20 tentativas\nNivel 2: 10 tentativas\nNivel 3: 5 tentativas\nQual nível você deseja? 1, 2 ou 3? '))
print(f'------------------------------\nOlá {nome}, Vamos começar?\n')

#Gerar um numero aleatório e condição para escolha do nível
numero_secreto = randint (1, 30)
rodada = 1
pontos = 1000

if nivel == 1:
    total_tentativas = 20
elif nivel == 2:
    total_tentativas = 10
elif nivel == 3:
    total_tentativas = 5


print(f'Você escolheu o Nível {nivel}!')


#Criar um loop para as tentativas e sistema de pontos
for rodada in range (1, total_tentativas+1):
    print(f'\n*****Tentativa {rodada} de {total_tentativas}*****\n')
    print(f'Pontos: {pontos}')
    chute =	int(input('Digite o seu numero: '))
    print('---------------------------------\nVocê digitou:', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    pontos = pontos - abs((chute - numero_secreto))

    if acertou:
        print(f'Pontos: {pontos}')
        print('Parabéns, Você acertou!!!!!!')
        break
    elif maior:
        print(f'Pontos: {pontos}') 
        print('O numero que você chutou é maior que o valor secreto!\n')
    elif menor:
        print(f'Pontos: {pontos}')
        print('O numero que você chutou é menor que o valor secreto!\n')
        


if not acertou:
    print(f'O numero secreto era {numero_secreto}')
    print('Tente Novamente!!!')

