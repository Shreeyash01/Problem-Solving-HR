n=int(input())
a=list(map(int,input().split()))

cnt=0
i=0
while(i<n-1) :
    if i<n-2 and a[i+2]==0 :
        cnt += 1
        i=i+2
    else:
        cnt += 1
        i=i+1

print(cnt)
