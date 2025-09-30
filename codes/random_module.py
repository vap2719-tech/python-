import random

names=input("enter names separated by commas:")
names_list=names.split(",")
#print(names_list)
length=len(names_list)
random_choice=random.randint(0,length-1)
print(f"{names_list[random_choice]} will pay bill")