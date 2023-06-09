#Faça um programa que leia um número inteiro N que indica a quantidade de números em um conjunto. 
#Em seguida, leia os N números inteiros que compõem esse conjunto. 
#O programa deve imprimir o comprimento de um segmento crescente de tamanho máximo. 
#Por exemplo, na sequência [3, 7, 4, 3, 6, 8, 9, 2, 5], o segmento crescente máximo é [3, 6, 8, 9], portanto seu comprimento é 4.
#Considere que um segmento de tamanho N é crescente quando X1 <= X2 <= ... <= XN.
n = int(input())

sequencia = 1
maior_sequencia = 1

if n > 0:

    num1 = int(input())

    i = 1
    while i < n:
        num2 = int(input())
        if num2 >= num1:
            sequencia += 1
        else:
            sequencia = 1
        if sequencia > maior_sequencia:
            maior_sequencia = sequencia
        num1 = num2            
        i += 1
    print(maior_sequencia)
    
else:
    print("Valor invalido.")            
