# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# s=a[0]
# r=a[1]
# q=a[2]
    
# for i in range(r):
#     l=b[s-1]
#     i=s-1
#     while(i>0):
#         b[i]=b[i-1]
#         i=i-1
#     b[0]=l
    
# for i in range(q):
#     c=int(input())
#     print(b[c])

a=list(map(int,input().split()))
b=list(map(int,input().split()))
n=a[0]
k=a[1]
q=a[2]

for i in range(q):
    c=int(input())
    d=(c+n-k)%n
    print(b[d])
