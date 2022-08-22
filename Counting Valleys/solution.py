n = int(input())
s = input()

a=0
cnt=0

for i in s:
    if i=="U":
        a += 1
        if a==0 :
            cnt=cnt+1
    else:
        a -=1

print(cnt)
