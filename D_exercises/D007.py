#Faça um programa que leia um valor inteiro N. 
#Após isso, leia N valores inteiros colocando-os em uma lista. 
#Em seguida, seu programa deve trocar os elementos dos índices adjacentes, par a par. 
#Por exemplo, deve ser trocado o elemento do índice 0 com o do índice 1, em seguida o elemento do índice 2 com o do índice 3 e assim sucessivamente. 
#Por fim, seu programa deve imprimir a lista resultante.

n = int(input())
arr = input().split()

i = 0
while i + 1 < len(arr):
    aux = arr[i]
    arr[i] = arr[i + 1]
    arr[i + 1] = aux
    i += 2

i = 0 
while i < n:
    print(arr[i], end=" ")
    i += 1    
