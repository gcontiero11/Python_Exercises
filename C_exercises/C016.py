#Faça um programa que leia um número inteiro N e imprima a soma de todos os números primos entre 1 e N (inclusive N).
n = int(input())
soma = 0       
while n > 0:
    divisores = 1
    i = 1
    if (n !=  2 and n % 2 == 0):
        n += (-1)
    else:    
        while i <= (n/2) and n > 1:
            if n % i == 0:
                divisores += 1
            i += 1    
        if divisores == 2 and n != 1:
            soma += n
        if n <= 3:
            n += (-1)
        else:        
            n += (-2)
print(soma)
