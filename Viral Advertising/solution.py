n=int(input())
a=5//2
cnt=0
for i in range(n):
    cnt=cnt+a
    b=a*3
    a=b//2
print(cnt)
