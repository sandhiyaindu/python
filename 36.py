m=str(input())
c1=0
for i in m:
    if i.isdigit()==False and i.isalpha()==False:
        c1=c1+1
print(c1)
