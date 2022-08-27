import string

a=list(map(int,input().split()))
s=input()
c=[]
d=[]
m=0

for i in s :
    b=string.ascii_lowercase.index(i)
    c.append(b)

for i in range(len(c)) :
    d.append(a[c[i]])
    
print(max(d)*len(s))
