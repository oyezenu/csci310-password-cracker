import hashlib

hashes = []
with open("salted_hashes.txt", "r") as f:
    for line in f:
        hashes.append(line.strip())

wordlist = set()
with open("rockyou.txt", "r", errors="ignore") as f:
    for line in f:
        wordlist.add(line.strip())

for word in wordlist:
    for line in hashes:
        parts = line.split(":")
        salt_hex = parts[0]
        stored_hash = parts[1]
        salt = bytes.fromhex(salt_hex)
        hashed_guess = hashlib.sha256(salt + word.encode()).hexdigest()
        if hashed_guess == stored_hash:
            print("The password is: " + word)
