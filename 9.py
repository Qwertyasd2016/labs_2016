input()
A = list(map(int, input().split(' ')))
c = A[0]+A[1]+A[2]
h = int(input())
for i in range(len(A)-h+1):
    if sum(A[i:i+3])>c:
        c = sum(A[i:i+3])
print(c)