import re

word = input("Enter your name: ")

check = re.search(r"\d", word)
if check is None:
    print("You're Welcome")
else:
    print('Not Welcome')

