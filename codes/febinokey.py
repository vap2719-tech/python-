n = 10
a,b = 0,1
#count=0
for i in range(n):
#while count < n:
    print(a,end=" ")
    a,b = b, a+b
    #count = count + 1