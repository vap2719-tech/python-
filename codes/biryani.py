size = input("what biryani u want(half/medium/full)?:")
bill = 0
if size == "hlaf" or size =="HALF":
    bill += 150
    print("half biryani price is 150rs")
elif size == "medium" or size == "MEDIUM":
    bill += 250
    print("medium biryani price is 250")
else:
    bill += 350
    print("full biryani price is 350")

add_currys_soops = input("do you want any curry/soops(Y/N)?:")
if add_currys_soops == "curry" or add_currys_soops =="CURRY":
    bill += 50
    print("curry prise is 50")
elif add_currys_soops == "soops" or add_currys_soops =="SOOPS":
    bill += 30
    print("soop prise is 30")
else:
    print("ok")
you_want_any_extra_rise=input("any extra somthing you want:")
if you_want_any_extra_rise == "half" or you_want_any_extra_rise == "HALF":
   bill += 70
   print("extra half rise prise is 100")
elif you_want_any_extra_rise == "full" or you_want_any_extra_rise == "FULL":
    bill += 100
    print("extra full rise prise is 100")
else:
    print("ok")
print(f"your finall bill is {bill}")
print("enjoy the recipe........")