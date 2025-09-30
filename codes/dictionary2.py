student_marks={
    "jenny":92,
    "priya":78,
    "sammi":56,
    "pooji":41,
    "hasya":99,
    "simma":34
    }
for i in student_marks:
    mark = student_marks[i]
    if mark >= 91:
        print(f"{i}: A+")
    elif mark >= 81:
        print(f"{i}: A")
    elif mark >= 71:
        print(f"{i}: B+")
    elif mark >= 61:
        print(f"{i}: B")
    elif mark >= 51:
        print(f"{i}: C")
    elif mark >= 41:
        print(f"{i}: D")
    else:
        print(f"{i}: F")
#print(student_marks)



          