'''a=15
def display():
    a=10 #local
    def show():
        print(a)  #function with in function
    show() # also local scope
display()
print(a) #global '''

'''
a,b=5,6
if a<b:
    c=a+b
print(c)
'''
'''
#global keyword

a=10
def display():
   a=20  
   print(a)
display()'''




for number in range(1,16):
  # print(number)
    if number%3==0:
        print("f")
    elif number%5==0:
        print("b")
    elif number%3==0 and number%5==0:
        print("f/b")
    else:
        print(number)
    