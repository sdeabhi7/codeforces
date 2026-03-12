'''
For a positive integer n let's define a function f:

f(n) =  - 1 + 2 - 3 + .. + ( - 1)nn

Your task is to calculate f(n) for a given integer n.

Input
The single line contains the positive integer n (1 ≤ n ≤ 1015).

Output
Print f(n) in a single line.

Examples

Input
4
Output
2

Input
5
Output
-3
'''

n = int(input())
if n % 2 == 0:
    print(n//2)
else:
    print(-(n+1)//2)