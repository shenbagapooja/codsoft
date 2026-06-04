import random

# this program generates a random password based on user input

length = int(input("Enter length of password: "))

# storing all possible characters for the password
lower = "abcdefghijklmnopqrstuvwxyz"   # lowercase letters
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   # uppercase letters
nums = "0123456789"                     # numbers
symbol = "!@#$%^&*"                    # special symbols

# combining all characters together
chars = lower + upper + nums + symbol

# generating the password using a loop
password = ""
for i in range(length):
    password += random.choice(chars)    # picking a random character each time

# displaying the final password
print("your password is :", password)
