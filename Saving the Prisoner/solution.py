# n=int(input())
# for i in range(n):
#     a=list(map(int,input().split()))
#     if a[1]>a[0]:
#         e=(a[0]+1)-a[2]
#         a[1]=a[1]-e
#         while(a[1]>a[0]):
#             a[1]=a[1]-a[0]
#         print(a[1])
#     else:
#         e=(a[2]-1)+a[1]
#         print(e)
        
n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    print((a[1]+a[2]-2)%a[0] +1)
