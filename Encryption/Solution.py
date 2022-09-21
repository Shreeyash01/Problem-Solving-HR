import math

s=input()
l=s.replace(" ","")
r=math.floor(math.sqrt(len(l)))
c=math.ceil(math.sqrt(len(l)))

string=''

for i in range(c):
    k=i
    for j in range(k,len(l),c):
        string+=l[j]
    string+=" "
    
print(string) 
