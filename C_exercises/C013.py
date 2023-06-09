#Faça um programa que leia um número inteiro positivo N.
#Após isso o programa deve ler N números inteiros e ao final da leitura imprimir o maior, menor e a soma dos números lidos.
n = int(input())
numero = int(input())
maior = numero
menor = numero
soma = numero
i = 1
while i <= n - 1:
    numero = int(input())
    soma = soma + numero 
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero    
    i += 1
print(maior)
print(menor)
print(soma)      
