n = int(input())
for i in range(n):
    k = input()
    y = len(k) // 2
    if len(k) % 2 == 0 and k[:y] == k[y:]:
        print('YES')
    else:
        print('NO')