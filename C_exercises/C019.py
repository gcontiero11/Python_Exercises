#Considere que seu computador só consegue realizar operações de soma ou subtração, ou seja, está com as operações de divisão e multiplicação inoperantes. 
#Faça um programa que leia dois números inteiros positivos A e B, onde A é a base e B é o expoente de uma potência.
#Após isso, calcule o valor da potência sem utilizar as operações inoperantes.
#Imprima o valor de A elevado a B.
#Obs: Não utilize bibliotecas matemáticas. No caso de python, não é permitido usar o operador **.
#Faça sua solução utilizando laço de repetição.
fator_1 = int(input())
fator_2= int(input())
i = 1
k = fator_1
potencia = fator_1
if fator_2 == 0:
    potencia = 1
elif fator_1 == 0 and fator_2 == 0:
    potencia = -1    
else:    
    while i < fator_2:
        j = 1
        while j < k:
            potencia += fator_1
            j += 1
        fator_1= potencia
        i += 1
print(potencia)
