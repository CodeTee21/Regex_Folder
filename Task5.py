import re

log = """
192.168.1.10 failed login
10.0.0.5 successful login
192.168.1.10 failed login
172.16.0.2 failed login
"""

# Extract IP addresses
ips = re.findall(r"\d+\.\d+\.\d+\.\d+", log)
print("IP Addresses:", ips)

check = re.findall(r"failed", log)
print(len(check))
