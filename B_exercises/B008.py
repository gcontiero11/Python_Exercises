#Faça um programa que leia três números inteiros A, B e C e imprima o maior deles.
a = int(input())
b = int(input())
c = int(input())
maior = a
if c > a  and c > b:
    maior = c
elif b > a:
    maior = b
print(maior)       
