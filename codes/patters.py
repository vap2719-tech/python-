'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
#printing squere pattern
'''
n=5
for i in range(n):
   for j in range(n):
        print("*",end=" ")  # end="" its print rectangle
   print()
   

#right angle triangle R increasing triangle
'''
*
* *
* * *
* * * *
* * * * *
# method one

rows=5
for i in range(1,rows+1):
    print("*"*i)
    
'''

# method two
'''
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()

#right angle triangle in left side
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)
'''

#decreasing triangle
'''
* * * * *
* * * * 
* * *
* *
*

n=5
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print() 
'''

# riht side triangle
'''
        *
      * *
    * * *
  * * * *
* * * * *

n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
'''

'''
* * * * *
  * * * * 
    * * * 
      * *
        *

n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
'''

'''
# hill pattern
n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):        # here we can take i+1 it print * * at top of the hill  
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
    '''

'''
#reverse hill pattern
n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()
'''

'''
# diamond patterns
n=5
for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):        # here we can take i+1 it print * * at top of the hill  
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

for i in range(n):
    for j in range(i+1):
         print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()

'''


'''
# print 1 triangle
n=5
for i  in range(n):
    for j in range(i+1):
        print("1",end=" ")
    print()
    '''
'''
#reverse of 1 triangle
n=5
for i  in range(n):
    for j in range(i,n):
        print("1",end=" ")
    print()
    '''
'''
# reverse right angle triangle 1
n=5
for i  in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("1",end=" ")
    print()
    '''
'''
# right side triangle 1
n=5
for i  in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("1",end=" ")
    print()
    '''
'''
# hill in 1
n=5
for i  in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("1",end=" ")
    for j in range(i+1):
        print("1",end=" ")
    print()
    '''
'''
#reverse hill 1
n=5
for i  in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
      print("1",end=" ")
    for j in range(i,n):
       print("1", end=" ")   
    print()

'''
'''
# pring patten starts with on e and increment 1
1
22
333
4444
55555

n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
    p+=1
    print()
    '''
'''
n=5
p=1
for i in range(n):
    for j in range(i,n):
        print(p,end=' ')
    p+=1
    print()
'''

'''
# starting with 5 in reverse hill  triangle
n=5
p=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n):
        print(p,end=" ")
    for j in range(i,n):
        print(p,end=" ")
    p-=1
    print()
'''

'''
# printing right angle pattern starts with 0 and incrament 2
n=5
p=0
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
    p+=2
    print()
'''

'''
#print triangle pattern even rows 1 & odd rows 2
n=5
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print("1",end=" ")
        else:
            print("2",end=" ")
    print()
    '''
'''
n=5

for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i):
        print()
    for j in range(i,n):
       if i%2==0:
          print("1",end=" ")
       else:
           print("2",end="")
    
    
    print
    '''
