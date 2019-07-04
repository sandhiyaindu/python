x=int(input())
sum=0
temp1=x
while(temp1>0):
  dig=temp1%10
  sum+=dig**3
  temp1//=10
if x==sum:
  print("yes")
else:
  print("no")
