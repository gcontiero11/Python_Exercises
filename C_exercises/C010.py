#Faça um programa que leia dois números inteiros e imprima o máximo divisor comum (MDC) entre eles.
#Dica: pesquise sobre o algoritmo de euclides.
numero1 = int(input())
numero2 = int(input())
while numero1 != 0 and numero2 != 0:
    if numero1 <= numero2:
        mdc = numero2
        numero2 = numero2 - numero1
    else:
        mdc = numero1
        numero1 = numero1 - numero2
print(mdc)
