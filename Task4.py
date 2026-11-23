import re

ask = input("Enter your phone number: ")
result = re.fullmatch(r"\d{11}", ask)
if result is not None:
    print("VALID NUMBER")
else:
    print("INVALID NUMBER")

