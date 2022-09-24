n,d=[int(r) for r in input().split()]
a=list(map(int,input().split()))
cnt=0
for i in range(0,n-2):
    b=a[i]+d
    c=a[i]+2*d
    if( (b in a) and (c in a) ):
        cnt+=1        
print(cnt)
