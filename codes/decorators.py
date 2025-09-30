# decoretors
# what is decorator: i means decorators are functions they are taken another function as input and return a new function

#def myfunction(fun):
 #   def function():
  # return function

#def  name():
 #   return "HELLO SYSTEM"
#print(name())


#mulltiple decorators call in python

#def myfunction(func):
 #   def myinner(x):
  #      return func(x).lower()
   # return myinner

#def function(name):
 #   return "my name is " + name


#def mycase():
 #   return "i am from btech" 
#print(function("ashok"))
#print(mycase())



# *args && **kwargs
#def myfunction(cham):
  #  def myupper(*args, **kwargs):
 #       return cham(*args, **kwargs).upper()
#        #return chamx(x).lower()
#    return myupper


#@myfunction
#def myfun(name):
 #   return "my name is" + name


#print(myfun("ashok"))



#example
#def changecase(func):
  #def myinner(*args, **kwargs):
  #  return func(*args, **kwargs).upper()
 # return myinner

#@changecase
#def myfunction(nam):
 # return "Hello " + nam

#print(myfunction("John"))




def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)  # Call the original function
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Greeting for {name}"

# Calling the decorated function
message = say_hello("Alice")
print(f"Function returned: {message}")
