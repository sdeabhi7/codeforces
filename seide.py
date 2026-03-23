n = int(input())
k = list(map(int, input().split()))
l = 0
r = n - 1
sereja = 0
dima = 0
y = 1
while l <= r:
    if y % 2 != 0 and y <= n:
        if k[l] > k[r]:
            sereja += k[l]
            l += 1
        else:
            sereja += k[r]
            r -= 1
    else:
        if k[l] > k[r]:
            dima += k[l]
            l += 1
        else:
            dima += k[r]
            r -= 1
    y += 1
print(sereja, dima)
# if l_sum > r_sum:
#     print(l_sum, r_sum)
# else:
#     print(r_sum, l_sum)
