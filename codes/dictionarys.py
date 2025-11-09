
#method_1 in dectionary
phone_no={"priya":9492621554,
          "ramya":9550390554,
          "simma":936734562}
print(phone_no["simma"])  

#method_2 in dectionary
phone_no=dict({"priya":9492621554,
          "ramya":9550390554,
          "simma":936734562})
print(phone_no)

#method_3 in dectionary
phone_no=dict([("priya",9492621554),
          ("ramya",9550390554),
          ("simma",936734562)])

print(phone_no)


#dict are mutable so we can easily updeted
phone_no={"priya":9492621554,
          "ramya":9550390554,
          "simma":936734562}
print(phone_no)
phone_no["ramya"]=9618200433
phone_no["sammi"]=9959488345
#print(phone_no)
print(phone_no.get("simma"))

print(phone_no.pop["priya"])  #deleted particular item

print(phone_no.popitem()  )# deleted any item randomly

print(phone_no.clear())  #it will rwturn nothing

print(phone_no.keys())   # it wil print only keys

print(phone_no.values())  #it will print only values

print(phone_no.items())   #


# length function
print(len(phone_no))


# this is the another method to copy
print(phone_no)
phone_no2=phone_no.copy()
print(phone_no2)


for i in phone_no:
    print(i)
    print(phone_no)