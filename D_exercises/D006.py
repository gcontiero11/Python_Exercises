#Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. 
#Em seguida, seu programa deve imprimir os N valores na ordem inversa que foram lidos.

n = int(input())
arr = input().split()

i = 0
while i < len(arr) // 2:
    aux = arr[i]
    arr [i] = arr[len(arr) - (1 + i)]
    arr[len(arr) - ( 1 + i)] = aux
    i += 1

i = 0
while i < len(arr):
    print(arr[i] , end=" ")
    i += 1
