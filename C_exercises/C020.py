#Faça um programa que leia um conjunto de valores que correspondem as idades de pessoas de uma comunidade.
#Quando o valor fornecido for um número negativo, significa que não existem mais idades para serem lidas.
#Após a leitura, seu programa deve informar:
#A média das idades das pessoas (com duas casas decimais)
#A quantidade de pessoas maiores de idade
#A porcentagem de pessoas idosas (considere quem uma pessoa idosa tem mais de 75 anos) (com duas casas decimais)
age = int(input())
maior_de_idade = 0
idoso = 0
leituras = 0
soma = 0
while age >= 0:
    leituras += 1
    soma += age
    if age >= 18:
        maior_de_idade += 1
    if age > 75:
        idoso += 1
    age = int(input())
media = soma/leituras
porcentagem = (idoso/leituras)*100
print(f"{media:.2f}")
print(maior_de_idade)
print(f"{porcentagem:.2f}%")
