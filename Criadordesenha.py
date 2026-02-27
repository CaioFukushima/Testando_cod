import random

#Criar senha
x=("abcdefghijklmnopqrstuvwxyz")
y=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
z=("123456789")
w=("!@#$%^&*()_+-=[]{}|;:,.<>?")

a=(x+y+z+w)

numero1 = int(input("Quantos caracteres precisa ter?")) #
resposta = input("Quer símbolos especiais? (sim/não) ") #
if resposta =="não":
     a = x + y + z
else:
     a = x + y + z +w
senha=""
for numero2 in range(numero1):
    senha=senha+random.choice(a)
print(senha)
