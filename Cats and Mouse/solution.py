n=int(input())

for i in range(n):
    d=list(map(int,input().split()))
    
    a=d[0]
    b=d[1]
    c=d[2]
    
    if abs(c-a)>abs(c-b) :
        print('Cat B')
    elif abs(c-a)<abs(c-b) :
        print('Cat A')
    else:
        print('Mouse C')
