#Faça um programa que leia dois números inteiros.
#Após isso, seu programa deve imprimir o resultado das seguintes operações: 
#1) o valor da divisão real do primeiro número lido pelo segundo (imprimir com duas casas decimais);
#2) o valor da divisão inteira do primeiro pelo segundo (imprimir como número inteiro);
#3) o valor do resto da divisão do primeiro pelo segundo (imprimir como número inteiro).
#ENTRADA
num1 = int(input())
num2 = int(input())
#PROCESSAMENTO
div1 = num1/num2
div2 = num1//num2
resto = num1 % num2
#SAIDA
print(f"{div1:.2f}")
print(div2)
print(resto)
