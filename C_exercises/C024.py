n = int(input())
bigger1 = 0
bigger2 = 0
i = 0
while i < n :
    number = int(input())
    if number >= bigger1 or i < 1:
        bigger2 = bigger1
        bigger1 = number
    elif number > bigger2:
        bigger2 = number
    i += 1
print(bigger1)
print(bigger2)
