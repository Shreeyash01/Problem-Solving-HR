import string

a=list(map(int,input().split()))
s=input()
e=[]
f=[]
m=0

for i in s :
    b=string.ascii_lowercase.index(i)
    e.append(b)

for i in range(len(e)) :
    f.append(a[e[i]])
    
print(max(f)*len(s))
