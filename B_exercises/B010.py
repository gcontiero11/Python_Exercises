#Sejam A, B e C os três lados de um triângulo. Faça um programa que leia o valor de três lados de um triângulo A, B e C.
#Seu algoritmo deve informar se o triangulo é: Escaleno (todos os lados diferentes); Isósceles (possui dois lados iguais); e Equilátero (todos os lados iguais);
#Não forma triângulo (quando a soma de dois lados é menor que o terceiro lado).
a = int(input())
b = int(input())
c = int(input())
triangulo = "INVALIDO"
if a < b + c and b < a + c and c < a + b:
    if a == b and a==c:
        triangulo = "EQUILATERO"
    elif a != b and a != c and b != c:
        triangulo = "ESCALENO"
    else:
        triangulo = "ISOSCELES"
print(triangulo)                    
