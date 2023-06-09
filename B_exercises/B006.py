#Faça um programa que leia os coeficientes a, b e c de uma equação do segundo grau ax² + bx + c.
#Após isso, calcule e imprima a soma das raízes da equação.
#Se as raízes não forem reais, imprima nan (use print(math.nan))
import math
a = float(input())
b = float(input())
c = float(input())
if a != 0:
    delta = b**2 - 4*a*c
    if delta < 0:
        print(math.nan)
    else:
        soma = -b/a
        print(f"{soma:.2f}")
else:
    print("esta não é uma equação de segundo grau")
