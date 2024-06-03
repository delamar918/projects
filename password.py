import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

let = []
sym = []
num = []
password = []

for l in range(1, nr_letters + 1):
  rand_l = random.choice(letters)
  let.append(rand_l)

for s in range(1, nr_symbols + 1):
  rand_s = random.choice(symbols)
  sym.append(rand_s)

for n in range(1, nr_numbers + 1):
  rand_n = random.choice(numbers)
  num.append(rand_n)

password = let + sym + num
random.shuffle(password)
final_password = ""
for char in password:
  final_password += char
print(f"Your password is: {final_password}")
