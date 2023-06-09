#Faça um programa que leia o salário fixo de um vendedor e o total de vendas efetuadas por ele no mês (em dinheiro).
#Sabendo que este vendedor ganha 18% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês.
#ENTRADA
salario = float(input())
venda = float(input())
#PROCESSAMENTO
salario = salario + venda*0.18
#SAÍDA
print(f"{salario:.2f}")
