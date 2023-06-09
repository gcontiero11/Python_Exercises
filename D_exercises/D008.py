#Faça um programa que leia um valor inteiro N. Após isso, leia duas listas A e B de tamanho N e coloque a soma das duas listas em uma terceira lista C. 
#Por exemplo C[0] = A[0] + B[0], C[1] = A[1] + B[1]. 
#Por fim, imprima a lista resultante C.

n = int(input())
arr1 = input().split()
arr2 = input().split()
arr_sum = []

for i in range(n):
    arr1[i] = int(arr1[i])
    arr2[i] = int(arr2[i])
    arr_sum.append(arr1[i] + arr2[i])

for i in range(len(arr_sum)):
    print(arr_sum[i], end=" ")
