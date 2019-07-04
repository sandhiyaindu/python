p=int(input())
r =[]
r=list(map(int,input('').split()))
r.sort()
for i in range(0,p,1):
  print(r[i],end=' ')
