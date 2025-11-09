student_data=[
   {
       
      "Name":"ram",
      "Roll_no":10,
      "Age":20,
      "Course":"python"
   },

   {
        
      "Name":"mohan",
      "Roll_no":12,
      "Age":21,
      "Course":"java"
   }
]


#print(student_data[0])

def new_student(name, roll_no, age, course):
    new_student_dict = {}
    new_student_dict["Name"] = name
    new_student_dict["Roll_no"] = roll_no
    new_student_dict["Age"] = age
    new_student_dict["Course"] = course
    student_data.append(new_student_dict)

new_student("ramya", 109, 18, "cyber")
print(student_data)



