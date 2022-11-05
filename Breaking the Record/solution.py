n=int(input())
c=list(map(int,input().split()))

b=c[0]
w=c[0]

cnt1=0
for i in range(len(c)) :
    if c[i]>b :
        cnt1 += 1
        b=c[i]
    else:
        continue
        
cnt2=0
for i in range(len(c)) :
    if c[i]<w :
        cnt2 += 1
        w=c[i]
    else:
        continue
    
print(cnt1,cnt2)
