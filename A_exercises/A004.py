#Faça um programa que leia o nome de um(a) aluno(a).
#Após isso, o programa deve ler duas notas de provas. 
#O programa deve calcular da média simples delas e escrever a saída conforme modelo abaixo.
#A média deve ser escrita com duas casas decimais.
#ENTRADA
nome = input()
a = float(input())
b = float(input())
#PROCESSAMENTO
media = (a+b)/2
#SAÍDA
print(f"{nome} obteve {media:.2f} de media")
