import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '/', '?', '~', '_', '-', '+', '=']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the Password Generator!")
let_letters = int(input("How many letters do you want?\n"))
sym_symbols = int(input("How many symbols do you want?\n"))
num_numbers = int(input("How many numbers do you want?\n"))

# Create a list to hold the password characters
password_list = []

# Add the requested number of random letters
for i in range(let_letters):
    password_list.append(random.choice(letters))

# Add the requested number of random symbols
for i in range(sym_symbols):
    password_list.append(random.choice(symbols))

# Add the requested number of random numbers
for i in range(num_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the list to mix the character types
random.shuffle(password_list)

# Join the list elements into a single string
final_password = "".join(password_list)

print(f"Your password is: {final_password}")