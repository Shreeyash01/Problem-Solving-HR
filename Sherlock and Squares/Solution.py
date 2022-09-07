
n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    cnt=0
    s1=a[0]**(0.5)
    
    if( s1 != int(s1)):
        c=int(s1)+1
    else:
        c=int(s1)
        
    s2=a[1]**(0.5)
    d=int(s2)
    cnt=d-c+1
    print(cnt)
    
# n=int(input())
# for i in range(n):
#     a=list(map(int,input().split()))
#     cnt=0
#     for j in range(a[0],a[1]+1) :
#         if (j**(0.5)==int(j**(0.5))):
#             cnt=cnt+1
#         else:
#             continue
#     print(cnt)
