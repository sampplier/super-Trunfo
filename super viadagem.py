import os
#biblioteca para a escolha aleatória
import random
#biblioteca para o delay
import time
#variavél pro delay
delay=1
#baralho de 20 cartas
cartas = [["Asta",70,20,80],["Luffy",70,20,90],["Shinra",100,50,100],["Manoel Gomes (Blue Pen)",1000,1000,1000],["Ace", 0, 0, 0],["Aki", 40, 80, 75],["Arthur Boyle ",70,20,100],["Capitão Pátria",100,40,80],["Sonic",100,60,30],["Denji",60,10,100],["Scizor",70,50,70],["Xaropinho",60,40,10],["ESCANOR",100,100,100],["Scaico",30,69,60],["Deku",70,80,77],["Dutinha Pressão",45,70,30],["Diuary",15,15,33],["Muzy",45,87,100],["Naruto",70,15,70],["Ednaldo Pereira",1000,1000,1000]]
#nome=0 e atributos de 1 até 3
#atributos são velocidade, inteligência e força
print("Olá, bem vindo ao jogo dos crias! ᕙ⁠(͡⁠°⁠‿⁠ ͡⁠°⁠)⁠ᕗ")
#pausa na execução para melhor visualização
time.sleep(delay)
nomeP1=input("Primeiro jogador, qual o seu nome? ")
time.sleep(delay)
nomeP2=input("Segundo jogador, qual o seu nome? ")
#pontos player 1
P1 = 1000
#baralho player 1
P1cards = []
#pontos player 2
P2 = 1000
#baralho player 2
P2cards = []
rodadas = 0
while rodadas < 5:
    #apenas na primera rodada pra não ter mais de quatro cartas sorteadas
    if rodadas <=0:
        for i in range(0, 4):
            #escolhe cartas aleatórias
            P1cards.append(random.choice(cartas))
             #remove a carta sorteada pra evitar repetição
            del cartas[cartas.index(P1cards[i])]
            #escolhe cartas aleatórias
            P2cards.append(random.choice(cartas))
            #remove a carta sorteada pra evitar repetição
            del cartas[cartas.index(P2cards[i])]
    #pergunta o valor a ser comparado, na carta de cima
    print("Olá", nomeP1)
    time.sleep(delay)
    #já entra na primeira carta e pergunta qual valor deve ser comparado
    escolhaP1 = P1cards[0][int(input("Qual atributo você quer disputar? 1 = Velocidade, 2 = Inteligência, 3 = Força "))]
    time.sleep(delay)
    print("Olá", nomeP2)
    time.sleep(delay)
    escolhaP2 = P2cards[0][int(input("Qual atributo você quer disputar? 1 = Velocidade, 2 = Inteligência, 3 = Força "))]
    #limpa o terminal
    os.system('cls')
    time.sleep(2)
    if rodadas<4:
        print("O número da rodada é:", rodadas)
    if rodadas==4:
        print("Rodada final!!")
    print(P1cards[0][0], escolhaP1, "VS", P2cards[0][0], escolhaP2)
    time.sleep(2)
    #compara as escolhas
    if escolhaP1 > escolhaP2:
        print(nomeP1, "venceu essa rodada ᕙ(⁠◍⁠•⁠ᴗ⁠•⁠◍⁠)ᕗ !!!")
        #descarta a carta jogada
        del P1cards[0]
        #adiciona a carta ao jogador vencedor
        P1cards.append(P2cards[0])
        #remove a carta do jogador perdedor
        del P2cards[0]
        #adiciona os pontos ao vencedor
        P1 += escolhaP1
        #subtrai a diferença do jogador que perdeu
        P2 -= escolhaP1 - escolhaP2
    elif escolhaP1 < escolhaP2:
        print(nomeP2, "venceu essa rodada ᕙ(⁠◍⁠•⁠ᴗ⁠•⁠◍⁠)ᕗ !!!")
        #descarta a carta jogada
        del P2cards[0]
        #adiciona a carta ao jogador vencedor
        P2cards.append(P1cards[0])
        #remove a carta do jogador perdedor
        del P1cards[0]
        #adiciona os pontos ao vencedor
        P2 += escolhaP1 
        #subtrai a diferença do jogador que perdeu
        P1 -= escolhaP2 - escolhaP1
    elif escolhaP1 == escolhaP2:
        print("O resultado é um empate ＼⁠(⁠°⁠o⁠°⁠)⁠／!!!")
        #descarta as duas e dá uma nova pra cada, na primeira posição
        del P1cards[0]
        del P2cards[0]
        P1cards.insert(0, random.choice(cartas))
        P2cards.insert(0, random.choice(cartas))
        #rodada anulada
        rodadas -= 1
    
    time.sleep(5)
    os.system('cls')
    rodadas += 1
#comparação final de pontos
if P1 > P2:
    print(nomeP1, "venceu o jogo!!!")
if P1 < P2:
    print(nomeP2, "venceu o jogo!!!")
if P1 == P2:
    print("Houve empate!!!")
print("Fim de jogo!!!!")
