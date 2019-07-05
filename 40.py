y=int(input())
p=1
q=1 
r=0
print()
while y!=0:
    p=q
    q=r
    r=p+q
    print(r,end=' ')
    y=y-1
    
