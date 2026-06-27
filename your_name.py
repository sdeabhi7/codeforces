#   author: sdeabhi



n = int(input())
for i in range(n):
    k = int(input())
    name = list(map(str, input().split()))
    if sorted(name[0]) == sorted(name[1]):
        print('Yes')
    else:
        print('No')