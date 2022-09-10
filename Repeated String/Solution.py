# s=input()
# n=int(input())

# a=[]
# while(len(a)<n):
#     for i in range(len(s)):
#         if (len(a)<n) :
#             a.append(s[i])
# print(a.count('a'))

s=input()
n=int(input())
k=int(s.count('a')*(n//len(s)) + s[:n%len(s)].count('a'))
print(k)


