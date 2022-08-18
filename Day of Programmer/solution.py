import math
import os
import random
import re
import sys

n=int(input())

if (n==1918):
    print('26.09.1918')
elif(n<1918):
    if (n%4==0):
        print('12.09.',n,sep='')
    else:
        print('13.09.',n,sep='')
else:
    if ((n%400==0) or (n%4==0 and n%100!=0)):
        print('12.09.',n,sep='')
    else:
         print('13.09.',n,sep='')
        
