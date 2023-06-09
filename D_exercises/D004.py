n = int(input())
if n > 0:
    arr = input().split()
    x = int(input())
    z = 0

    position = -1

    i = 0
    while i < len(arr):
        if x == int(arr[i]) and z != 1:
            position = i
            z = 1
        i += 1
    print(position)
else:
    print()
