#   author: sdeabhi



t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if n == k:
        print(2 * n)
    else:
        print((2 ** (n - k + 1)) + 2 * (k - 1)) 

# r = int(input())
# for i in range(r):
#     n, k = map(int, input().split())
#     t = n - k + 1
#     s = 1
#     for j in range(t):
#         s *= 2
#     s += (n - t) * 2
#     print(s)