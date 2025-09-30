numbers = input("enter a numbers:")
numbers_list = numbers.split()
#print(numbers_list)
count = 0
for numb in numbers_list:
    count += 1
print(count)
for i in range(count):
    numbers_list[i] = int(numbers_list[i])
#print(numbers_list[i])
max_number = numbers_list[0]
for number in numbers_list:
    if number > max_number:
        max_number = number
print(max_number)
        
