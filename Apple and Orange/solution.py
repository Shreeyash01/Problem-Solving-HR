e = list(map(int, input().split()))
f = list(map(int, input().split()))
g = list(map(int, input().split()))
h = list(map(int, input().split()))
i = list(map(int, input().split()))

# x=np.array(h) +f[0]
x = []
for j in range(len(h)):
    z = h[j] + f[0]
    x.append(z)
# y=np.array(i) +f[1]
y = []
for j in range(len(i)):
    z = i[j] + f[1]
    y.append(z)

cnt1 = 0
cnt2 = 0

for j in range(len(x)):
    if x[j] >= e[0] and x[j] <= e[1]:
        cnt1 += 1

for j in range(len(y)):
    if y[j] >= e[0] and y[j] <= e[1]:
        cnt2 += 1

print(cnt1)
print(cnt2)
