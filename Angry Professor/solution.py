n=int(input())

for i in range(n):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cnt=0
    for j in range(len(b)):
        if b[j]<=0 :
            cnt += 1
    if cnt>=a[1] :
        print('NO')  
    else:
        print('YES')      
    
