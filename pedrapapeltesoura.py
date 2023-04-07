import random
import os
import time
pontos_do_jogador=0
pontos_do_computador=0
boo=False
print("Joque pedra papel e tesoura com o computador, o primeiro que fazer 3 pontos vencerá!")
while (pontos_do_computador<3 or pontos_do_jogador<3) and boo==False:
    print("Pontos do computador: ",pontos_do_computador,"\nPontos do jogador: ",pontos_do_jogador)
    #receber a escolha do jogador
    escolha_jogador=str(input("Insira uma escolha (pedra, papel ou tesoura):\n"))
    while bool(escolha_jogador=="pedra") is False and bool(escolha_jogador=="papel") is False and bool(escolha_jogador=="tesoura") is False:
        print("Input não suportado, por favor, tente novamente\n")
        escolha_jogador=str(input("Insira uma escolha (pedra, papel ou tesoura):\n"))
    #decidir a escolha do computador
    pc=["pedra", "papel", "tesoura"]
    escolha_pc=random.choice(pc)
    #colocar todas as possibilidades(cada variável b é um resultado possível)
    b1=bool(escolha_jogador=="pedra" and escolha_pc=="tesoura")
    b2=bool(escolha_jogador=="papel" and escolha_pc=="pedra")
    b3=bool(escolha_jogador=="tesoura" and escolha_pc=="papel")
    b4=bool(escolha_jogador=="pedra" and escolha_pc=="papel")
    b5=bool(escolha_jogador=="papel" and escolha_pc=="tesoura")
    b6=bool(escolha_jogador=="tesoura" and escolha_pc=="pedra")
    b7=bool(escolha_jogador==escolha_pc)
    #se o jogador vencer
    if (b1 or b2 or b3) is True:
        print("Jogador:",escolha_jogador,"\nComputador:",escolha_pc,"\nPonto para o jogador!")
        pontos_do_jogador+=1
        time.sleep(2)
        os.system('cls')
    elif (b4 or b5 or b6) is True:
        #se o computador vencer
        print("Jogador:",escolha_jogador,"\nComputador:",escolha_pc,"\nPonto para o computador!")
        pontos_do_computador+=1
        time.sleep(2)
        os.system('cls')
    elif b7 is True:
        #se der empate
        print("Jogador:",escolha_jogador,"\nComputador:",escolha_pc,"\nEmpate! Nenhum ponto será distribuido")
        time.sleep(2)
        os.system('cls')
    if pontos_do_jogador==3 or pontos_do_computador==3:
        boo=True
#printando o resultado final
if pontos_do_jogador>pontos_do_computador:
    print("Pontos do computador: ",pontos_do_computador,"\nPontos do jogador: ",pontos_do_jogador)
    print("Vitória do jogador!")
elif pontos_do_computador>pontos_do_jogador:
    print("Pontos do computador: ",pontos_do_computador,"\nPontos do jogador: ",pontos_do_jogador)
    print("Vitória do computador!")
