import re

print("===== Password Complexity Checker =====")

password = input("Enter Password: ")

length = len(password) >= 8
uppercase = re.search(r"[A-Z]", password)
lowercase = re.search(r"[a-z]", password)
number = re.search(r"[0-9]", password)
special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

score = 0

if length:
    score += 1

if uppercase:
    score += 1

if lowercase:
    score += 1

if number:
    score += 1

if special:
    score += 1

print("\nPassword Analysis")

if score == 5:
    print("Strong Password")

elif score >= 3:
    print("Medium Password")

else:
    print("Weak Password")
    
    