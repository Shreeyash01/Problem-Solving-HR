from collections import Counter

n=int(input())
a=list(map(int,input().split()))

d=Counter(a)
b=list(d.values())
b.remove(max(b))

print(sum(b))
