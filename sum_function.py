# input ,num1=5,num2=10

def function(num1,num2):
    return num1+num2
    #print(num1+num2)
result=function(5,10)
print(result)
#function(5,10)


#find area of circle
# #input r=5
# area=3.14*r**2

def function(r):
    print(3.14*r*r)
function(5)


#find quadratic equetion
#input a=1,b=2,c=3

def quadratic(a,b,c):
    d=(b**2)-4*a*c
    root1=(-b+(d**(0.5)))/2*a
    root2=(-b-(d**(0.5)))/2*a
    print(root1,root2)
x=int(input("enter value of a:"))
y=int(input("enter aavalue of b:"))
z=int(input("enter value of c:"))

quadratic(a = x,b = y,c = z)



#converting units into fharanhit


def temp(c):
    f=c*9/5+32
    k=273+c
    print(f,k)
x=int(input("enter a temp in units:"))
temp(x)
