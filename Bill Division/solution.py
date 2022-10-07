a=list(map(int,input().split()))

b=list(map(int,input().split()))

c=int(input())

d=(sum(b)-b[a[1]])/2

if d==c :
    print('Bon Appetit')
else:
    print(int(c-d))
