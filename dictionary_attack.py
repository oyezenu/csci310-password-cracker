import hashlib

hashes = []
with open("hashes.txt", "r") as f:
    for line in f:
        hashes.append(line.strip())


wordlist = set()
with open("rockyou.txt", "r", errors="ignore") as f:
    for line in f:
        wordlist.add(line.strip())


for word in wordlist:
    hashed_word = hashlib.sha256(word.encode()).hexdigest()
    if hashed_word in hashes:
        print("The password is: " + word)
