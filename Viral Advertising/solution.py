m=int(input())
b=5//2
cnt=0
for i in range(m):
    cnt=cnt+b
    c=b*3
    b=c//2
print(cnt)
