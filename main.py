#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

random_password = []

# Letters
for i in range(0, nr_letters):
  random_password.append(letters[random.randint(0, len(letters)-1)])

# Numbers
for i in range(0, nr_numbers):
  random_password.append(numbers[random.randint(0, len(numbers)-1)])

# Symbols
for i in range(0, nr_symbols):
  random_password.append(symbols[random.randint(0, len(symbols)-1)])

# Randomize array and export as string
password_length = nr_letters + nr_numbers + nr_symbols
final_password = ""

while len(final_password) < password_length:
  final_password+= random_password.pop(random.randint(0, len(random_password)-1)) 
  
print(final_password)
