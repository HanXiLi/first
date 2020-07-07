# 解一元二次方程
from __future__ import division
import math
def jieFangCheng(a,b,c):
    x=b*b-4*a*c
    if x>0:
        y=math.sqrt(x)
        x1=(-b+y)/(2*a)
        x2=(-b-y)/(2*a)
        return x1,x2
    elif x==0:
        x1=-(b/(2*a))        
        return x1
    else:
        return False
if __name__=="__main__":
    result=jieFangCheng(1,2,1)
    if result==False:
        print("该方程无解！")
    else:
        print(result)