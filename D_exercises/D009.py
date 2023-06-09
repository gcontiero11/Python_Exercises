#Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros colocando-os em uma lista. 
#Em seguida, leia dois valores I e J que correspondem duas posições na lista. 
#Ao final, o programa deve escrever a soma dos elementos entre I e J, incluindo os elementos de I e J. Se I ou J forem posições inválidas na lista, imprimir a mensagem INVALIDO.

n = int(input())
arr = input().split()
posicao = input().split()
i = int(posicao[0])
j = int(posicao[1])
if (i > len(arr) - 1  or j > len(arr) - 1) or (i < 0 or j < 0):
    print("INVALIDO")
else:        
    if i > j:
        aux = i
        i = j
        j = aux
    soma = int(arr[j])     
    for x in range(i , j):
        arr[x] = int(arr[x])
        soma += arr[x]
    print(soma)
