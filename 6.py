n = int(input())
A = list(map(int, input().split(' ')))
for i in range(n):
    k = 0
    m = 0
    for j in range(n):
        if A[i] < A[j]:
            k += 1
        elif A[i] > A[j]:
            m += 1
    if k == n // 2 and m == n // 2:
        print(A[i])