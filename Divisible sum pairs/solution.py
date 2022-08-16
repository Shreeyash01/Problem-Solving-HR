c=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()

cnt=0
for i in range(len(a)) :
    j=i+1  
    for j in range(j,len(a)):
        if ((a[i]+a[j])%(c[1])==0) :
            cnt += 1
        else:
            continue
        
print(cnt)
