#   author: sdeabhi



n , k = map(int, input().split())
s = list(map(int, input().split()))
value = 0
s.sort()
for i in range(2, len(s), 3):
    if s[i] + k <= 5:
        value += 1
print(value)