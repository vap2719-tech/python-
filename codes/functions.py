#define a function
def my_function():
    print("this is a function example")


#fuction calling
def my_function():
    print("this is ashok's laptop")
my_function()

#arguments
def my_function(fname):
    print(fname+"reference")
my_function("email")
my_function("ashok")

#number of arg's
def my_function(fname,iname,jname):
    print(fname+" "+iname+jname)
my_function(fname="email",iname="ashok",jname="pooja")

#recursion
#def tri_recursion(k):
 #   if(k>2):
  #      print("rsult")
   # else:
    #    result=0
     #   return result
    #print("recursion example:")
    #tri_recursion(4)

#defauil arg's



#arbitary ag's
def add(*numbers):
    c=0
    for i in numbers:
        #c += i
        c = c + i
        print(f"sum is{c}")
        
add(5,6,7)

#return values
def add(a,b):
    return a + b
result = add(5,3)
print(result)
    #print(a+b)
#add(5,6)

# fuction 
def greet(name, message="Hello"):
        print(f"{message}, {name}!")
greet("ashok")


# eample
def add_to_list(item, my_list=None):
        if my_list is None:
            my_list = []
        my_list.append(item)
        return my_list

print(add_to_list(1))  
print(add_to_list(2))