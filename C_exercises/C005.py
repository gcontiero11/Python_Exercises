#Faça um programa que leia uma sequência de números inteiros do usuário até que ele digite o valor zero. 
#Quando o valor zero for digitado, o programa deve imprimir o resultado em três linhas: 
#1ª linha) Soma dos valores pares da sequência; 
#2ª linha) Soma dos valores ímpares da sequência; 
#3ª linha) soma de todos os valores da sequência.
n = int(input())
s_par = 0
s_inpar = 0
soma = 0
while n != 0:
    if n % 2 == 0:
        s_par = s_par + n
    else:
        s_inpar = s_inpar + n
    soma = soma + n
    n = int(input())
print(s_par)
print(s_inpar)
print(soma)           
