num=int(input())
revers=0
while(num>0):
  digit=num%10
  revers=revers*10+digit
  num=num//10
print(revers)
