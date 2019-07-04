b1,b2=map(int,input().split())
for m in range(b1+1,b2):
  sum=0
  temp1=m
  while temp1>0:
    digit=temp1%10
    sum+=digit**3
    temp1//=10
  if m==sum:
    print(m,end=' ')
