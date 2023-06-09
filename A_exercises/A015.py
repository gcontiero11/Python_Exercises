#Faça um programa que leia um número inteiro E de eleitores de um município, um número inteiro B que representa o número de votos brancos, um número N de votos nulos e um número V de votos válidos.
#O programa deve calcular e escrever o percentual que cada um representa em relação ao total de eleitores, além da porcentagem de ausentes.
#Formate sua saída conforme exemplos abaixo.
e = int(input())
b = int(input())
n = int(input())
v = int(input())
Brancos = (b/e) * 100
Nulos = (n/e) * 100
Validos = (v/e) * 100
Ausentes = 100-Brancos-Nulos-Validos
print(f"Nulos: {Nulos:.2f}%")
print(f"Brancos: {Brancos:.2f}%")
print(f"Validos: {Validos:.2f}%")
print(f"Ausentes: {Ausentes:.2f}%")
