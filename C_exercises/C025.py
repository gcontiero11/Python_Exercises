#Faça um programa que leia um número inteiro e positivo N. Após isso leia N números inteiros.
#Ao fim, imprima 1 se a sequência de números lidos estão ordenados em forma crescente e -1 se estão ordenados de forma decrescente.
#Se não estão ordenados, imprima 0. Considere que uma sequência de tamanho N é crescente quando X1 <= X2 <= ... <= XN e decrescente quando X1 >= X2 >= ... >= XN.
#No caso desse exercício, se todos os valores lidos forem iguais, considere como um segmento crescente.
n = int(input())

Crescente = True
Decrescente = True
num1 = int(input())

i = 1
while i < n:
    num2 = int(input())
    if num2 > num1:
        Decrescente = False
    elif num2 < num1:
        Crescente = False
    num1 = num2
    i += 1

if Crescente == True and Decrescente == True:
    ordem = 1    
elif Crescente == True:
    ordem = 1      
elif Decrescente == True:
    ordem = -1
else:
    ordem = 0
print(ordem)            
