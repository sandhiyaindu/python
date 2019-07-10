def longest(st1,st2):
        if(st1 in st2):
            return st1
        else:
            return longest(st1[0:len(st1)-1],st2)
j = int(input())
a= []
for _ in range(0,j):
    a.append(input())
a.sort()
print(longest(a[0],a[j-1]))
