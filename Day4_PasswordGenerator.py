#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_length = nr_numbers + nr_symbols + nr_letters
password_length_currently = 0
nr_letters_used = 0
nr_symbols_used = 0
nr_numbers_used = 0
password = ''

while password_length_currently != password_length:
    KeySelect = random.randint(0,2)
    if KeySelect == 0 and nr_letters_used != nr_letters:
        password += random.choice(letters)
        nr_letters_used += 1
        password_length_currently += 1
    elif KeySelect == 1 and nr_symbols_used != nr_symbols:
        password += random.choice(symbols)
        nr_symbols_used += 1
        password_length_currently += 1
    elif KeySelect == 2 and nr_numbers_used != nr_numbers:
        password += random.choice(numbers)
        nr_numbers_used += 1
        password_length_currently += 1
    else:
        pass

print(password)