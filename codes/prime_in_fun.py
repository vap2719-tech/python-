#import math

def prime(number):
    is_prime=True
    if number == 1:
         is_prime=False

     #for i in range(2,number-1):    #method-1
    for i in range(2,round(number/2)+1):     #method-2
    # for i in range(2,math.ceil(number/2)+1):   #round function
        if number % i == 0:
            is_prime=False
    if is_prime == True:
          print("its  a prime number")
    else:
          print("its not a prime number")           

n=int(input("enter a number:\n"))  
prime(n)  
