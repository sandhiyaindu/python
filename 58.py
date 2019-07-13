p,q=map(int,input().split())
count1=0
arr=list(map(int,input().split()))[:p]
for j in arr:
  if j==q:
    count1+=1
if(count1!=0):
  print("yes")
else:
  print("no")
