import hashlib

hashes = []
with open("iterated_hashes.txt", "r") as f:
    for line in f:
        hashes.append(line.strip())

wordlist = set()
with open("rockyou.txt", "r", errors="ignore") as f:
    for word in f:
        wordlist.add(word.strip())

for word in wordlist:
    for line in hashes:
        parts = line.split(":")
        salt_hex = parts[0]
        stored_hash = parts[1]
        salt = bytes.fromhex(salt_hex)
        hashed = hashlib.sha256(salt + word.encode()).hexdigest()
        for i in range(10000):
            hashed = hashlib.sha256(hashed.encode()).hexdigest()
        if hashed == stored_hash:
            print("The password is: " + word)
