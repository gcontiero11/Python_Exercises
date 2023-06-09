#Na matemática, um número primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo.
#Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.
#Faça um programa que leia um número inteiro positivo N e imprima 1 se ele for primo e 0 caso contrário.
n = int(input())
i = 1
divisores = 1
while i <= (n/2):
    if n != 2 and n % 2 == 0:
        divisores = 0
    elif n % i == 0 and n != i:
        divisores += 1
    i += 1
if divisores == 2:
    primo = 1
else:
    primo = 0
print(primo)            
