#Ana gosta muito de matemática e de brincar com números.
#Ela definiu o conceito de "Número da Ana. 
#Se um número inteiro não negativo N é produto de três números inteiros consecutivos então N é um "Número da Ana".

#Faça um programa que leia um número inteiro não negativo N e imprima "S" se for um "Número da Ana" e "N" caso contrário.
#Por exemplo, 120 é um "Número da Ana", pois é resultado da multiplicação 4 x 5 x 6.
n = int(input())

numero_ana = "N"

i = 1
while i * (i + 1) * (i + 2) <= n :
    if n == i * (i + 1) * (i + 2):
        numero_ana = "S"
    i += 1

print(numero_ana)
