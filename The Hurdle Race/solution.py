a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=max(b)

if a[1]<c :
    print(c-a[1])
else:
    print(0)
