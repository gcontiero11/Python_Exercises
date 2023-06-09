#Osmar adora chocolates e vai para a loja com N dinheiro no bolso.
#O preço de cada chocolate é C. A loja oferece um desconto: para cada M (sempre maior que 1) embalagens que ele dá para a loja, ele ganha um chocolate grátis.
#Quantos chocolates Osmar consegue comer?
#Por exemplo:
#Para N=10, C=2, M=5, ele pode comprar 5 chocolates por $10 e trocar as 5 embalagens por mais 1 chocolate, fazendo com que o número total de chocolates que ele pode comer seja 6.
#Faça um programa que leia N, C e M e imprima a quantidade de chocolates que Osmar pode comer.
import math
n = int(input())
c = int(input())
m = int(input())
embalagens = math.trunc(n / c)
chocolates = embalagens
while embalagens >= m:
    embalagens -= m
    embalagens += 1
    chocolates += 1  
print(chocolates)
