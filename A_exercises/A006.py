#Em épocas de crise, comerciantes estão oferecendo descontos para aumentarem suas vendas.
#Faça um programa que leia o valor total da compra e um valor de desconto (de 0 a 100, representando a porcentagem de desconto).
#O programa de escrever o valor da compra com o desconto aplicado. Escreva a saída com duas casas decimais.
#ENTRADA
valor = float(input())
desc = float(input())
#PROCESSAMENTO
valor = valor * (1 - desc/100)
#SAÍDA
print(f"{valor:.2f}")
