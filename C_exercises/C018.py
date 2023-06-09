#Faça um programa que leia dois números inteiros positivos A e B e faça o cálculo de multiplicação de A e B usando apenas a operação de soma.
#Imprima o resultado ao final.
a = int(input())
b = int(input())
i = 0
soma = 0
while i < b:
    soma += a
    i += 1
print(soma)
