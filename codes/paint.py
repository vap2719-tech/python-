import math

def paint_calculation(height,width,cover):
    area=height*width
    no_of_cans=math.ceil(area/cover)
    print(f"you have {no_of_cans} cans required")

h=int(input("enter the height of wall:\n"))
w=int(input("enter a widht of wall:\n"))
coverage=7
paint_calculation(width=w,height=h,cover=coverage)
