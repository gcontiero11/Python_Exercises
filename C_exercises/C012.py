#Faça um programa que leia um número inteiro positivo N.
#Após isso o programa deve ler N números inteiros e ao final da leitura imprimir o maior deles.
n = int(input())
numero = int(input())
maior = numero
i = 1
while i < n :
    numero = int(input())
    if numero > maior:
        maior = numero
    i += 1
print(maior)
