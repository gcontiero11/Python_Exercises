#Faça um algoritmo que leia 3 valores inteiros A, B e C. 
#Coloque-os em ordem crescente (ou seja, ao final A deve armazenar o menor valor, C o maior e B o valor do meio). 
#Utilize o modelo abaixo apresentado no final do exercício, modificando apenas o processamento
#ENTRADA
a = int(input())
b = int(input())
c = int(input())
#PROCESSAMENTO
if a > b and a > c:
    maior = a
    a = c
    c = maior
elif b > c:
    maior = b
    b = c
    c = maior
if a > b:
    meio = a
    a = b
    b = meio    
#SAÍDA
print(a)
print(b)
print(c)
