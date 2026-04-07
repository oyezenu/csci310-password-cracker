import hashlib
import itertools
import string

characters= string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


hashes = []
with open("hashes.txt", "r") as f:
    for line in f:
        hashes.append(line.strip())

for length in range(1, 5):
    for guess in itertools.product(characters, repeat=length):
        guess_str = "".join(guess)
        hashed_guess = hashlib.sha256(guess_str.encode()).hexdigest()
        if hashed_guess in hashes:
            print("The password is: " + guess_str)
