p,intg1=input().strip().split(" ")
intg1=int(intg1)
j=0;
while j<len(p)-1 and intg1:
	if(p[j]>p[j+1]):
		intg1-=1
		p=p[:j]+p[j+1:]
		if(j!=0):
			j-=1
	else:
		j+=1
s=p[:len(p)-intg1]
print(s)
