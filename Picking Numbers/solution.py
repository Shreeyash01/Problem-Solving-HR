n=int(input())
a=list(map(int,input().split()))

from collections import Counter
d=Counter(a)

best=0

for i in range(99):
    best=max(d[i]+d[i+1],best)

print(best)
