#Faça um programa que leia um valor inteiro N.
#Após isso, leia N valores inteiros.
#Em seguida leia um número inteiro X.
#Ao fim escreva o número de vezes que o número X foi lido do usuário.

n = int(input())
arr = input().split()
x = int(input())
aparicoes = 0

i = 0
while i < n:
    if x == int(arr[i]):
       aparicoes += 1
    i += 1

print(aparicoes)
