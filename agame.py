n = int(input())
a = 0
b = 0
for i in range(n):
    k, y = map(int, input().split())
    if k > y:
        a += 1
    elif y > k:
        b += 1
if a > b:
    print("Mishka")
elif b > a:
    print("Chris")
else:
    print("Friendship is magic!^^")