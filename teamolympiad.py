n = int(input())
k = list(map(int, input().split()))
ones = []
twos = []
threes = []
for i in range(n):
    if k[i] == 1:
        ones.append(i + 1)
    elif k[i] == 2:
        twos.append(i + 1)
    else:
        threes.append(i + 1)
teams = min(len(ones), len(twos), len(threes))
print(teams)
for i in range(teams):
    print(ones[i], twos[i], threes[i])