n=int(input())
a=list(map(int,input().split()))

b=a[0]
w=a[0]

cnt1=0
for i in range(len(a)) :
    if a[i]>b :
        cnt1 += 1
        b=a[i]
    else:
        continue
        
cnt2=0
for i in range(len(a)) :
    if a[i]<w :
        cnt2 += 1
        w=a[i]
    else:
        continue
    
print(cnt1,cnt2)
