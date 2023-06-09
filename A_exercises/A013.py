#Faça um programa que leia um número inteiro S que representa uma quantidade de segundos.
#Seu programma deve imprimir quatro valores inteiros, que representem a quantidade de segundos S em dias, horas, minutos e segundos.
#Por exemplo, 188365 segundos representam 2 dias, 4 horas, 19 minutos e 25 segundos.
#Dica: lembre-se dos operadores resto e divisão inteira.
#ENTRADA
s = int(input())
#PROCESSAMENTO
dia = s // 86400
hor = (s % 86400) //  3600
min = (s % 86400) % 3600 // 60
s = (s % 86400) % 3600 % 60
#SAÍDA
print(dia,hor,min,s)
