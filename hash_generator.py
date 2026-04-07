import hashlib
import os

passwords = ["password123", "hello", "letmein"]

with open("salted_hashes.txt", "w") as f:
	for password in passwords:
	   salt = os.urandom(16)
	   salted_password = salt + password.encode()
	   hashed = hashlib.sha256(salted_password).hexdigest()
	   salt_hex = salt.hex()
	   f.write(salt_hex + ":" + hashed + "\n")

print("Salted hashes saved to salted_hashes.txt")


