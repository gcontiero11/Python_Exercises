#A avenida principal da cidade de Algoritmopolis possui limite de velocidade de L km/h.
#Se o motorista ultrapassar essa velocidade, é aplicado uma multa de R$ M, mais R$ A por cada km acima do limite.
#Faça um programa que leia o limite L, o valor da multa M, o valor adicional A e a velocidade V captada pelo radar e informe o valor total da multa.
#Considere L e V sempre como números inteiros.
#Apresente a resposta com duas casas decimais.
l = int(input())
m = float(input())
a = float(input())
v = int(input())
if v > l:
    m = m + (v-l) * a
    print(f"{m:.2f}")
else:
    m = 0
    print(f"{m:.2f}")    
