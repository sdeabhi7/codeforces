n = int(input())
for i in range(n):
    k = input()
    if k.count('A') > 2:
        print('A')
    else:
        print('B')