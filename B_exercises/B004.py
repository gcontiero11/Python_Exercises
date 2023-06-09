#Um motorista de Uber estipula o preço de uma determinada viagem dada a quantidade de quilômetros percorrida. 
#Para viagens de até X km, é cobrado um valor R$ V1 por km.
#Acima de Y km, é cobrado o valor R$ V2. 
#Faça um programa que leia X, V1, V2 e a quantidade de quilômetros A da viagem e imprima o valor total com duas casas decimais.
x = int(input())
v1 = float(input())
v2 = float(input())
a = float(input())
if x >= a:
    preço = v1 * a
    print(f"{preço:.2f}")
else:
    preço = v2 * a
    print(f"{preço:.2f}")
