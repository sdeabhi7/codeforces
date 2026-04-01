n = int(input())
for i in range(n):
    k = int(input())
    s = input()
    y = []
    t = 0
    for i in s:
        if i not in y:
            y.append(i)
            t += 2
        else:
            t += 1
    print(t)