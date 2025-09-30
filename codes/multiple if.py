height = int(input("enter your height:?"))
bill = 0
if height > 4:
    print("you can allowed to ride")
    age = int(input("enter your age please:?"))
    if age < 12:
        bill = 150
        print("your token price is 150")
    elif age < 18:
        bill = 250
        print("your token price is 250")
    else:
        bill = 500
        print("your token price is 500")
    want_photo = input("do you want any photo")
    if want_photo == "yes" or want_photo == "YES":
       bill = bill + 50
       print(f"your total is {bill} bill")
    
else:
    print("you can't allowed to ride")
print("enjoy a wanderfull ride....")