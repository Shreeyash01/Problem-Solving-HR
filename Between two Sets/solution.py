a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

n = len(b) - 1
d = []


for i in range(b[n], c[0]+1):
    cnt3 = 0
    for j in range(len(b)):
        if i % b[j] == 0:
            cnt3 += 1

    if cnt3==len(b) :
        d.append(i)

cnt2 = 0
for i in range(len(d)):
    cnt1 = 0
    for j in range(len(c)):
        if c[j] % d[i] == 0:
            cnt1 = cnt1 + 1

    if cnt1 == len(c):
        cnt2 = cnt2 + 1

print(cnt2)
