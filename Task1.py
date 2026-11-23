import re

text = "I am learning Python C50"


result = re.findall(r"\d", text)

print(result)
