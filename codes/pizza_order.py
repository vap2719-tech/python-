size = input("which size pizza you want S/M/L:")
bill = 0
if size == "S" or size == "s":
   bill += 100
   print("small pizza size is 100 RS")
elif size == "M" or size == "l":
   bill += 200
   print("medium pizza size is 200 RS")
else:
   bill += 300
   print("large pizza size is 300 RS")

add_pepperoni = input("do you want extra pepperoni(Y/N)?:")
if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S" or size == "s":
       bill += 30
    else:
      bill += 50

extra_cheese =  input("do you want extra cheese (Y/N)?:")
if extra_cheese == "Y" or extra_cheese == "y":
   bill += 20

print(f"your final bill is {bill}")
print("enjoy the piza...time...")