n=int(input())
a=list(map(int,input().split()))

b={x:a.count(x) for x in a}
c=max(sorted(b.values()))

for key,value in b.items():
    if value==c :
        print(key)
        break
