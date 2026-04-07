import hashlib
import os

passwords = ["password123", "hello", "letmein"]

with open("iterated_hashes.txt", "w") as f:
	for password in passwords:
	   salt = os.urandom(16)
	   hashed = hashlib.sha256(salt + password.encode()).hexdigest()
	   for i in range(10000):
	      hashed = hashlib.sha256(hashed.encode()).hexdigest()
	   salt_hex = salt.hex()
	   f.write(salt_hex + ":" + hashed + "\n")

print("Salted hashes saved to iterated_hashes.txt")


