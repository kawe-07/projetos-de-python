import random

def numero_secreto():

    numero_secreto = random.randint(1,100)

    return numero_secreto

print("bem-vindo ao Jogo da adivinhação")
print("Um numero aleatorio entre 1 e 100 é sorteado.")

segredo = numero_secreto()
cont = 0

while(True):
    
    palpite = int(input("digite seu palpite sobre o numero secreto: "))
    cont += 1

    if (palpite > segredo):

        print(f"seu palpite foi {palpite}")
        print("o numero secreto é menor!")

    elif( palpite < segredo):

        print(f"seu palpite foi {palpite}")
        print("o numero secreto é maior!")
   
    else:
        print("VOCÊ ACERTOUUU!!!")
        print(f"foram {cont} tentativas")
        break
