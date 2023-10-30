from random import *

#o usuário muda essa variável para terminar o jogo 
jogando = True

placar = 0

#imprima as instruções do jogo
print('''
Vinte e Um!
=========
Tente fazer exatamente 21 pontos!
''')

while jogando == True:

    #escolha aleatoriamente um número (entre 1 e 10)
    numero = randint(1, 10)
    placar += numero

    #mostre ao jogador qual número ele obteu e qual o seu placar atual
    print("O seu número é:", numero)
    print("O seu placar atual é:", placar)


    #pergunte ao jogador se ele quer continuar jogando
    print("\nVocê que jogar de novo? (s/n)")    

    resposta = input().lower().strip()
    if resposta == 'n':
        jogando = False
    if resposta == 's':
        continue


if placar == 21:
    print("\nParabéns!!!\n")

print("\nObrigado por jogar.")
print("\nSua pontuação final é de", placar)
