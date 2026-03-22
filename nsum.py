n = int(input())
for i in range(n):
    a, b, y = map(int, input().split())
    if a + b == y or a + y == b or b + y == a:
        print('YES')
    else:
        print('NO')