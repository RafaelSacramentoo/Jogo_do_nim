


#VARIAVEL DO TIPO DO JOGO
tipo_jogo= 0
while tipo_jogo == 0:

#MENU DE OPÇÕES# 
    print("Bem vindo ao jogo do NIM! Escolha")
    print("")   
    print("1- para jogar uma partida isolada")
    print("2- para jogar um campeonato")


#OPÇÃO DO ÚSUARIO
tipo_jogo= int(input("Sua opção:"))
print("")


#DECIDE O TIPO DE JOGO
if tipo_jogo == 1:
    print('Você escolheu partida isolada')
    partida()
    break

elif tipo_jogo == 2:
    print("Você escolheu jogar um campeonato")
    campeonato()
    break

else :
    print("Sua opcão não é valida")
    tipo_jogo == 0




#VEZ DO USUÁRIO
print("Vez do usuario")






#FUNÇÃO PARTIDA FOI CHAMADA
def partida():
    print("")

#SOLICITA AO USUARIO O VALOR DE X E Y
    n= int(input("Digite o número de peças:"))
    m= int(input("Digite o número de peças por jogada"))

#VARIAVEL PARA A VEZ DO COMPUTADOR INICIAR
pc_inicia= True


#DECIDE QUEM INICIA  O JOGO
if n % (m+1) == 0: 
pc_inicia = False



#EXECUTANDO  ENQUANTO TEM PEÇAS NO JOGO 

while n>0:
    if pc_inicia :
        jogada= computador_escolhe_jogada(n,m)
        pc_inicia= False
        print("Computador retirou {} peças." format (jogada))
        
    else:
        jogada= computador_escolhe_jogada(n,m)
        pc_inicia= True
        print("Você retirou {} peças.". format (jogada))
            
            



