n = int(input())
for i in range(n):
    k = input()
    value = 0
    for i in k:
        if i in '0123456789':
            value += int(i)
    print(value)