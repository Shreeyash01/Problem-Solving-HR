n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
if len(a) == 1:
    if a[0] == b[0]:
        cnt = cnt + 1
else:
    for i in range(len(a) -b[1]+1):
        j = i
        sum = 0
        for j in range(j, j + b[1]):
            sum = sum + a[j]

        if sum == b[0]:
            cnt = cnt + 1

print(cnt)
