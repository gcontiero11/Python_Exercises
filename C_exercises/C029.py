#Faça um programa que leia um número inteiro não negativo N e imprima "S" se ele é palíndromo e "N" caso contrário. 
#Um número é palíndromo quando lido da esquerda para a direita é igual ao ser lido da direita para a esquerda. 
#Exemplos: 37173, 1221.

#Obs: Faça seu programa utilizando apenas números inteiros.
    #Não é permitido converter o número para string.
n = int(input())

conversor = n
inverso = 0
palindromo = "N"

while conversor != 0:
    inverso = inverso * 10
    inverso = inverso + conversor % 10
    conversor = conversor // 10
if inverso == n:
    palindromo = "S"
print(palindromo)
