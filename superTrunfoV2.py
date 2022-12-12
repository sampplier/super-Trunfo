import random
import time
delay=1
cartas = [["Asta",70,20,80], ["Luffy",70,20,90], ["Shinra",100,50,100],
          ["Manoel Gomes (Blue Pen)", 100, 100, 100], ["Ace", 0, 0, 0],
          ["Aki", 40, 80, 75], ["Arthur Boile ", 70, 20, 100],
          ["Capitão Pátria", 100, 40, 80], ["Sonic", 100, 60, 30],
          ["Denji", 60, 10, 100], ["Scizor", 70, 50, 70],
          ["Xaropinho", 60, 40, 10],["ESCANOR ", 100, 100, 100],
          ["Scaico", 30, 69, 60], ["Deku", 70, 80, 77],
          ["Dutinha Pressão", 45, 70, 30], ["Diuary", 15, 15, 33],
          ["Muzy", 45, 87, 100], ["Naruto", 70, 15, 70],
          ["Ednaldo Pereira", 100, 100, 100]]
#nome=0, atributos de 1 até 3
#atributos são velocidade, inteligência e força
print("Olá, bem vindo ao jogo dos crias! ᕙ⁠(͡⁠°⁠‿⁠ ͡⁠°⁠)⁠ᕗ")
time.sleep(delay)
nomeP1=input("Primeiro jogador, qual o seu nome? ")
time.sleep(delay)
nomeP2=input("Segundo jogador, qual o seu nome? ")
P1 = 1000
P1cards = []
P2 = 1000
P2cards = []
#random 4 cartas pra cada no inicio
#escolher a caracteristica
rodadas = 0
while rodadas < 5:
    if rodadas == 0:
        for i in range(0, 4):
            #escolhe cartas aleatórias
            P1cards.append(random.choice(cartas))
            #remove a carta sorteada pra evitar repetição
            P2cards.append(random.choice(cartas))
            #pergunta o valor a ser comparado, na carta de cima
    print("Olá", nomeP1)
    time.sleep(delay)
    escolhaP1 = P1cards[0][int(input("Qual atributo você quer disputar? 1 = Velocidade, 2 = Inteligência, 3 = Força "))]
    time.sleep(delay)
    print("Olá", nomeP2)
    time.sleep(delay)
    escolhaP2 = P2cards[0][int(input("Qual atributo você quer disputar? 1 = Velocidade, 2 = Inteligência, 3 = Força "))]
    time.sleep(2)
    print(P1cards[0], "VS", P2cards[0])
    time.sleep(2)
    if escolhaP1 > escolhaP2:
        print(nomeP1, "venceu essa rodada!!!")
        P1cards.append(P2cards[0])
        del P2cards[0]
        P1 += escolhaP1
        P2 -= escolhaP1 - escolhaP2
        #append cartas ao jogador vencedor
        #subtrai a diferença do jogador que perdeu
    elif escolhaP1 < escolhaP2:
        print(nomeP2, "venceu essa rodada!!!")
        P2cards.append(P1cards[0])
        del P1cards[0]
        P2 += escolhaP1 
        P1 -= escolhaP2 - escolhaP1
        #append cartas ao jogador vencedor
        #subtrai a diferença do jogador que perdeu
    elif escolhaP1 == escolhaP2:
        print("O resultado é um empate!!!")
        #descarta as duas e dá uma nova pra cada
        del P1cards[0]
        del P2cards[0]
        P1cards.insert(0, random.choice(cartas))
        P2cards.insert(0, random.choice(cartas))
        #rodada anulada
        rodadas -= 1
    rodadas += 1
    print("O número da rodada é:", rodadas)
    if P1 > P2:
        print("O jogador 1 venceu!!!")
    if P1 < P2:
        print("O jogador 2 venceu!!!")
    if P1 == P2:
        print("Houve empate!!!")
