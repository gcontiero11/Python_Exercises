from turtle import position


n = int(input())

arr = input().split()


i = 0
while i < n :
    if i == 0:
        maior = arr[i]
        position = 0
    elif arr[i] > maior:
        if maior != arr[i]:
            position = i
        maior = arr[i]
    i += 1    
print(maior)
print(position)    
