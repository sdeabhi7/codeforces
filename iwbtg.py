n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
k = list(set(a[1:] + b[1:]))
if 0 in k:
    k.remove(0)
if len(k) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')