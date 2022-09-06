str1 = input()
str2 = input()
k = int(input())

i = 0
while i<len(str1) and i<len(str2) and str1[i]==str2[i]:
    i+=1
    
s1 = len(str1[i:])
s2 = len(str2[i:])

s=s1+s2

if s>k:
    print("No")
elif s==k:
    print("Yes")
elif (len(str1)+len(str2))-k<=0:
    print("Yes")
elif abs((len(str1)+len(str2))-k)%2==0:
    print("Yes")
else:
    print("No")
    
# str1 = input()
# str2 = input()
# n = int(input())

# a=[]
# b=[]

# for i in range(len(str1)):
#     a.append(str1[i])
# for i in range(len(str2)):
#     b.append(str2[i])

# if len(a)>=len(b):
#     for i in range(len(b)):
#         if str1[i]==str2[i] :
#             a.remove(str1[i])
#             b.remove(str2[i])
#         else:
#             break
# else:
#     for i in range(len(b)):
#         if str1[i] == str2[i]:
#             a.remove(str1[i])
#             b.remove(str2[i])
#         else:
#             break

# s=len(a)+len(b)

# if s<=n :
#     print('Yes')
# else:
#     print('No')
