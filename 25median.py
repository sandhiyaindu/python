import math
y=int(input())
x =[]
x=list(map(int,input('').split()))
x.sort()
l=len(x)
mid=(l/2)
r=math.floor(mid)
print(x[r])
