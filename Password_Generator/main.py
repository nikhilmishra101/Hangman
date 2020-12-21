import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X' , 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
type_password = input("Which type of password do you want? Easy or hard\n")

password = []

for letter in range(1,nr_letters+1):
  password.append(random.choice(letters))

for number in range(1,nr_numbers+1):
  password.append(random.choice(numbers))

for symbol in range(1,nr_symbols+1):
  password.append(random.choice(symbols))


if type_password.lower() == "easy":
  easy_password = ''.join(password)
  print("Here is your password:",easy_password)
elif type_password.lower() == "hard":
  random.shuffle(password)
  hard_password = ''.join(password)
  print("Here is your password:",hard_password)
else:
  print("Please enter the correct type")






