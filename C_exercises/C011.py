#Faça um programa que leia um número inteiro e positivo X.
#Após isso, leia sucessivos números inteiros positivos, até que um número negativo seja lido.
#Ao fim, escreva o número de vezes que o número inicial X foi lido do usuário.
x = int(input())
num = 0
num_vezes = 0
while num >= 0:
    num = int(input())
    if num == x:
        num_vezes += 1
print(num_vezes)        
