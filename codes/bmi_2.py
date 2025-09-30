weight = (input("enter yuour weight:"))
height = (input("enter your height:"))
BMI = round(int(weight) / float(height)**2)
#print(BMI)
if BMI < 18.5:
    print(f"your BMI is {BMI} and you are under weighted")
elif BMI < 22.5:
    print(f"your BMI is {BMI} and you are normal")
elif BMI < 26:
    print(f"your BMI is {BMI} and you are over weight")
elif BMI < 30:
    print(f"your BMI is {BMI} and you are obese")
else:
    print(f"your BMI is {BMI} and you are clinically obese")
    print("TATA TATA")