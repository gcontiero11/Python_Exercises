temp_list=(input().split())

amount = 0
above = 0

i = 0
while i < 7:
    amount += int(temp_list[i])
    i += 1

average = amount/7

i = 0
while i < 7:
    if int(temp_list[i]) > average:
        above += 1
    i += 1    
print(above)
