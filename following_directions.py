n = int(input())
for i in range(n):
    y = 'NO'
    ud, rl = 0, 0
    k = int(input())
    s = input()
    for i in s:
        if i == 'U':
            ud += 1
        elif i == 'D':
            ud -= 1
        elif i == 'L':
            rl -= 1
        elif i == 'R':
            rl += 1
        if ud == 1 and rl == 1:
            y = 'YES'
            break
    print(y)