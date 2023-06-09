#Faça um programa que leia um número inteiro (assuma que esse número terá 4 digitos obrigatoriamente) e inverta esse número.
#Por fim escreva o número invertido.
#O seu programa deve apenas manipular números inteiros. 
#Não é permitido usar strings, lista, etc.
num = int(input())
unidade = num // 1000 # 3
dezena = num % 1000 // 100 * 10 #60
centena = num % 1000 % 100 // 10 * 100 #700
milhar = num % 1000 % 100 % 10 * 1000 #4000
num2 = milhar + centena + dezena + unidade
print(num2)
