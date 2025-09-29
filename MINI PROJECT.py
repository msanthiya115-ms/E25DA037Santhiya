import re
pwd = input("Enter password: ")
score = 0
if len(pwd) >= 8:
    score += 1
if re.search(r"[a-z]", pwd):
    score += 1
if re.search(r"[A-Z]", pwd):
    score += 1
if re.search(r"[0-9]", pwd):
    score += 1
if re.search(r"[^A-Za-z0-9]", pwd):
    score += 1
    
if score <= 2:
    print("Weak Password")
elif score == 3 or score == 4:
    print("Medium Password")
else:
    print("Strong Password")


