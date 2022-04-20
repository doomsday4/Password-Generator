import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
level = input("Do you wand the password to be Strong or Easy? ")

if level == "Easy":
 password = ""
 for i in range(0, nr_letters):
   password += random.choice(letters)

 for j in range(1, nr_symbols + 1):
   password += symbols[random.randint(0, len(symbols)-1)]

 for k in range(0, nr_numbers):
   password += numbers[random.randint(0, len(numbers)-1)]

   print(password)


elif level == "Strong":
  pass_list = []
  pass_list += random.choice(letters)

  for j in range(1, nr_symbols + 1):
    pass_list += symbols[random.randint(0, len(symbols)-1)]

  for k in range(0, nr_numbers):
    pass_list += numbers[random.randint(0, len(numbers)-1)]
  random.shuffle(pass_list)
  strong_pass = ""
  for char in pass_list:
    strong_pass += char
  print(strong_pass)  
else:
  print("Error")


