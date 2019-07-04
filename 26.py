c=int(input())
v=list(map(int,input().split()[:c]))
v.sort()
for p in v:
  print(p,end=" ")
