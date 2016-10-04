n = int(input())
A = [0]*n
B = [0]*n
for i in range(n):
    N = list(map(int, input().split(' ')))
    A[i] = N[0]
    B[i] = N[1]
T = int(input())
c = 0
for i in range(n):
    if A[i] <= T <= B[i]:
        c += 1
print(c)