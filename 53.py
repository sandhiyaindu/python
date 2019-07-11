p=int(input())
n=0
i=0
while(p>0):
    i=p%10
    n=n+i
    p=p//10
print(n)
