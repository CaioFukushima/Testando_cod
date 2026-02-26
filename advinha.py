import random

numero = random.randint(1, 10)
chute = 0
tentativas = 0

print("--- Jogo de Adivinhação ---")

while chute != numero:
    chute = int(input("Digite um número: "))
    tentativas += 1
    
    if chute == numero:
        print(f"Congratulations! Você acertou em {tentativas} tentativas.")
    elif chute > numero:
        print("Muito alto! Tente um menor.")
    else:
        print("Muito baixo! Tente um maior.")
