n = int(input())
value = 'Timur'
k = ''.join(sorted(value))
for i in range(n):
    l = int(input())
    s = input()
    if l <= 5 and ''.join(sorted(s)) == k:
        print('YES')
    else:
        print('NO')