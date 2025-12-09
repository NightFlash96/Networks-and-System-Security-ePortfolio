import os, hashlib, time

def hash_sha256_salt(password: str, salt: bytes) -> str:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(salt + password.encode())
    return sha256_hash.hexdigest(), salt.hex()

secret_password = input("Enter a password to crack: ")
# secret_password = "ilovemycat"
salt = os.urandom(2) # two byte salt is more than enough

hashed_password = hash_sha256_salt(secret_password, salt)

salt_combinations = []

# for a in range(256):
#     value = bytes([a])
#     salt_combinations.append(value)

for a in range(256):
    for b in range(256):
        value = bytes([a, b])
        salt_combinations.append(value)

print("Total salt combinations to try:", len(salt_combinations))

file = open("100k_common_passwords.txt", "r")

common_passwords = [line.strip() for line in file.readlines()]

counter = 0
cracked = False
start = time.time()
for j in salt_combinations:
    if cracked:
        break
    for i in common_passwords:
        counter += 1

        guess = hash_sha256_salt(i.strip(), j)
        print("Attempt #", counter, "Trying password:", i.strip(), "with salt:", j.hex(), "->", guess)

        if guess == hashed_password:
            cracked = True
            print("Password cracked! The password is:", i.strip())
            print("It took", counter, "attempts to crack the password.")
            end = time.time()
            print("Time taken to crack the password:", round(end - start, 2), "seconds.")
            break

if not cracked:
    print("Password not found in wordlist")
    print("Tried", counter, "combinations.")
    print("Time taken to attempt all combinations:", round(time.time() - start, 2), "seconds.")