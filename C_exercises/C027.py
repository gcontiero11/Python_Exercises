#Faça um programa que leia um número inteiro positivo N e imprima "S" se for um número perfeito e "N" caso contrário. 
#Um número é perfeito se for igual à soma de seus divisores positivos diferentes de N. 
#Por exemplo, 6 é perfeito, pois 1 + 2 + 3 = 6.
n = int(input())

soma = 0
perfeito = "N"

i = 1
while i <= (n/2):
    if n % i == 0:
        soma += i
    i += 1    
if soma == n:
    perfeito = "S"
print(perfeito)    
