n = int(input())
a = []
a.append(0)
b = list(map(int, input().split()))
for k in range(len(b)):
    a.append(b[k])
    
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == a[j]:
            for y in range(1, n+1):
                if a[j] == a[a[y]]:
                    print(y)
                else:
                    continue
        else:
            continue
