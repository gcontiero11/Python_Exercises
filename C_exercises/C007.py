#Faça um programa que leia dois números inteiros não negativos A e B, onde A é a base e B é o expoente de uma potência.
#Após isso, calcule e imprima o valor de A elevado a B. 
#Não utilize bibliotecas matemáticas. 
#No caso de python, não é permitido usar o operador **.
#Faça sua solução utilizando laço de repetição.
a = int(input())
b = int(input())
potencia = 1
i = 1
while i <= b:
    potencia = potencia * a
    i = i + 1
print(potencia)
