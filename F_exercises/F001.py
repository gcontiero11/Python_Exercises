#Faça um programa que leia as dimensões N e M de uma matriz A, representando o número de linhas e colunas respectivamente. 
#Após isso, leia N x M valores em apenas uma linha, colocando-os na matriz A.
#Por fim, imprima a matriz em formato matricial.
n = input().split()
num_linhas= int(n[0])
num_colunas= int(n[1])
numeros= input().split()

aux = num_colunas
mat = []

j = 0
for i in range(num_linhas):
    linha = []

    while j < num_colunas:
        linha.append(numeros[j])
        j += 1
    mat.append(linha)
    num_colunas = num_colunas + aux

num_colunas = aux

for i in range(num_linhas):
    for j in range(num_colunas):
        print(mat[i][j], end=" ")
    print()
