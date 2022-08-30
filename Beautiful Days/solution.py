a=list(map(int,input().split()))
cnt=0
for i in range(a[0],a[1]+1):
    d=str(i)
    b= d[::-1]
    c= abs(i - int(b))
    if c%a[2]==0 :
        cnt += 1
    else:
        continue
print(cnt)    
