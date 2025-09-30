def room_paint(height,width,cover):
    no_of_cans=round(height*width/cover)
    print(f"your room has {no_of_cans} will required")


h = int(input("enter a room of height:"))
w = int(input("enter a width of room:"))
coverage=23
room_paint(height=h,width=w,cover=coverage)   