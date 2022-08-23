a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

m=0
bgt=a[0]+1

for i in range(len(b)):
    for j in range(len(c)):
        if ((b[i]+c[j])>m) and ((b[i]+c[j])<bgt) :
            m=b[i]+c[j]
        else:
            continue
            
if m==0 :
    print(-1)
else:
    print(m)
