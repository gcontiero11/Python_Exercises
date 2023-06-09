#Faça um programa que leia dois números inteiros X e Y e imprima todos os números de X até Y, seguidos nos números de Y até X. Se X for maior que Y, imprima INVALIDO.
x = int(input())
y = int(input())
if x <= y:
    for numero in range(x,y+1):
        print(numero)
    for numero in range(y,x-1,-1):
        print(numero)
else:
    print("INVALIDO")
