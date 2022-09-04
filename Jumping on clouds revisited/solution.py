l=list(map(int,input().split()))
a=list(map(int,input().split()))
n=l[0]
k=l[1]

i=k%n
e=100-1-a[i]*2
while i != 0:
        i = (i + k) % n
        e -= 1 + a[i]*2
print(e)
