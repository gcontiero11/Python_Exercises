#Um matemático italiano da idade média conseguiu modelar o ritmo de crescimento da população de coelhos através de uma sequência de números naturais que passou a ser conhecida como Sequência de Fibonacci. 
#O n-ésimo número da sequência de Fibonacci Fn é dado pela seguinte formula: Fi = Fi-1 + Fi-2.
#O resultado é a sequência {1, 1, 2, 3, 5, 8, 13, 21, ...}.
#Faça um programa que leia um número inteiro positivo N e imprima os N primeiros números da sequência de Fibonacci, todos em uma linha separados por espaço.
f = int(input())
f1 = 0
f2 = 0
fn = 1

i = 0
while i < f:
    print(fn , end=" ")
    f1 = f2
    f2 = fn
    fn = f1 + f2
    i = i + 1
