n = input()
y = list(map(str, input().split()))
k = 'No'
for i in n:
    if i in ''.join(y):
        k = 'Yes'
        break
print(k)