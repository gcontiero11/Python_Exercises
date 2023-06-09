#Faça um programa que leia um número inteiro positivo N e imprima a soma dos dígitos desse número. 
#Por exemplo, se a entrada for 358, a saída será 16 (3 + 5 + 8). 
#Obs: Não é permitido transformar os números em strings, ou seja, resolva o problema apenas utilizando operações matemáticas válidas.
numero1 = int(input())
soma = 0
unidades = 1
resto = 0
resto2 = 0
while unidades <= numero1*10:
    resto = numero1 % unidades
    soma = int(soma + (resto - resto2)//(unidades*0.1))
    resto2 = resto
    unidades = unidades * 10
print(f"{soma}")
