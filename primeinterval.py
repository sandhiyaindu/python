e,t=map(int,input().split())
for m in range(e+1,t):
  if m>1:
    for i in range(2,m):
      if(m%i)==0:
        break
    else:
     print(m,end=" ")  
