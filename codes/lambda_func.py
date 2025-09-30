#lambda functins
#examople 1
x=lambda a: a+10
print(x(3))


#example 2
x=lambda a,b : a*b
print(x(2,3))


#example 3
x=lambda a,b,c:a+b+c
print(x(2,3,4))


# doubler
def myfunc(n):
    return lambda a : a * n
mydoubler=myfunc(2)
print(mydoubler(11))

#tripular
def myfunc(n):
   return lambda a:a*n
mytripular=myfunc(3)
print(mytripular(33))


def functions(n):
    return lambda a:a+n
doubler=functions(2)
tripular=functions(3)
print(doubler(23))
print(tripular(33))