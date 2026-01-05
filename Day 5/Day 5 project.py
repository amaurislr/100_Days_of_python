import random

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%','&', '(',')', '*', '+']

count = int
count_letter = int(input("How many letters would you like in your password?"))
count_numbers = int(input("How many numbers would you like in your password?"))
count_symbols = int(input("How many symbols would you like in your password?"))
password = ""

for count_letter_ in range(1, count_letter + 1) and range (1, count_numbers +1) and range (1, count_symbols +1):
   count = random.choice(letters) + random.choice(numbers) + random.choice (symbols)
   print(f"{count}", end="")

