import re

email = input("ENTER YOUR EMAIL: ")

result = re.search(r"\w+@\w+\.com",email)

if result is not None:
    print("Valid Mail")
else:
    print("Invalid Mail")

