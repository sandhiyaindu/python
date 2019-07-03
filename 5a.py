x,y,z=input().split()
if(x>=y and y>=z):
  print(x)
elif(y>=x and y>=z):
  print(y)
else:
  print(z)
