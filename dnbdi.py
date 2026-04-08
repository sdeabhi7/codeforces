n = int(input())
for i in range(n):
    k = int(input())
    s = input()
    y = {}
    t = 'YES'
    for i in range(len(s)):
        if s[i] not in y:
            y[s[i]] = i
        elif abs(y[s[i]] - i) > 1:
            t = 'NO'
            break
        else:
            y[s[i]] = i
    print(t)