#Faça um programa que leia o valor dos catetos de um triângulo retângulo e calcule a hipotenusa, de acordo com o Teorema de Pitágoras.
#Pesquise como extrair a raiz quadrada de um número.
#ENTRADA
ca1 = float(input())
ca2 = float(input())
#PROCESSAMENTO
Hip = (ca1**2+ca2**2)**0.5
#SAÍDA
print(f"{Hip:.2f}")
