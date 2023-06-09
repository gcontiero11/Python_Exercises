#Faça um programa que leia três números reais A, B e C de uma equação do segundo grau, considerando: Ax^2 + Bx + C.
#Seu programa deve calcular e imprimir as as raízes da equação.
#Assuma que delta sempre será positivo.
#ENTRADA
a = float(input())
b = float(input())
c = float(input())
#PROCESSAMENTO
delta = b**2 - 4*a*c
x1 = (-b + delta**0.5)/(2*a)
x2 = (-b - delta**0.5)/(2*a)
#SAÍDA
print(f"{x1:.2f}")
print(f"{x2:.2f}")
