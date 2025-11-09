def add(a,b):
    c=a+b
    return(c)
#print(add(3,4))
resualt=add(3,4)
print(resualt) 



# title case means each word of the frsit letter should be capital
def my_name(f_name,l_name):
    my_name_f_name=f_name.title()
    my_name_l_name=l_name.title()

    #print(f"{my_name_f_name},{my_name_l_name}")
    return(f"{my_name_f_name},{my_name_l_name}")
resualt=my_name("ashok", "vemula")
print(resualt)


# return multiple values from a function
import statistics
def mean_median_mode(L1):
    return [statistics.mean(L1),statistics.median(L1),statistics.mode(L1)] 
#resualt=(mean_median_mode([3,4,5,66,77,56,42,71,82,6]))
a,b,c=(mean_median_mode([3,4,5,66,77,56,42,71,82,6]))
 
print(f"mean is {a}\n median is {b}\n mode is {c}")




# addition example of return function
def add(a,b):
    if a==0 & b==0 :
      return "you enter 0 for both variables"
    else:
        return a+b


var1=int(input("enter a var1:\n"))
var2=int(input("enter a var2:\n"))
result=add(var1,var2)
print(result)


