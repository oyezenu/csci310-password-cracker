import hashlib
import os

passwords = ["password123", "hello", "letmein"]

# Simple hashes
with open("hashes.txt", "w") as f:
    for password in passwords:
        hashed = hashlib.sha256(password.encode()).hexdigest()
        f.write(hashed + "\n")
print("Simple hashes saved to hashes.txt")

# Salted hashes
with open("salted_hashes.txt", "w") as f:
    for password in passwords:
        salt = os.urandom(16)
        salted_password = salt + password.encode()
        hashed = hashlib.sha256(salted_password).hexdigest()
        salt_hex = salt.hex()
        f.write(salt_hex + ":" + hashed + "\n")
print("Salted hashes saved to salted_hashes.txt")

# Iterated hashes
with open("iterated_hashes.txt", "w") as f:
    for password in passwords:
        salt = os.urandom(16)
        hashed = hashlib.sha256(salt + password.encode()).hexdigest()
        for i in range(10000):
            hashed = hashlib.sha256(hashed.encode()).hexdigest()
        salt_hex = salt.hex()
        f.write(salt_hex + ":" + hashed + "\n")
print("Iterated hashes saved to iterated_hashes.txt")

