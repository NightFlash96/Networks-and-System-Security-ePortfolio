import sys
import hashlib, bcrypt

password = input("Enter password to hash: ")

def hash_password_md5(password: str) -> str:
    md5_hash = hashlib.md5(password.encode())
    return md5_hash.hexdigest()

def hash_password_sha256(password: str) -> str:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password)
    return sha256_hash.hexdigest()

def hash_password_bcrypt(password: str) -> str:
    return