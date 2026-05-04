n = int(input())
for i in range(n):
    s = list(map(int, input().split()))
    s1 = max(s[0], s[1])
    s2 = max(s[2], s[3])
    if s1 > min(s[2], s[3]) and s2 > min(s[0], s[1]):
        print('Yes')
    else:
        print('No')