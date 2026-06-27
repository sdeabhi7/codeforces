#   author: sdeabhi



n = int(input())
for i in range(n):
    nums, price, offer = map(int, input().split())
    t = 2 * price
    if t < offer:
        print(nums * price)
    elif nums % 2 != 0:
        print(int(nums / 2) * offer + price)
    else:
        print(int(nums / 2) * offer)