def c(r):
    try:
        float(r)
        print("yes")
    except:
        print("No")
r=str(input())
c(r)
