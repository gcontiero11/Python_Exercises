#Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. 
#A cada valor lido, o programa deve inserir em uma lista A se o valor for par e em uma lista B se o valor for ímpar.
#Ao fim, escreva as duas listas resultantes, na primeira linha a lista A e na segunda a lista B.

n = int(input())
A = []
B = []
arr = input().split()

i = 0
while i < len(arr):
    arr[i] = int(arr[i])
    i += 1

i = 0
while i < len(arr):
    if arr[i] % 2 == 0:
        A.append(arr[i])
    else:
        B.append(arr[i])
    i += 1    

i = 0
while i < len(A):
   print(A[i] ,end=" ")
   i += 1

print()

i = 0
while i < len(B):
    print(B[i], end=" ")
    i += 1

print()
