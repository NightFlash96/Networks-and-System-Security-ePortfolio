while True:
    import string, math

    password = input("Enter your password: ")

    strength = 0
    pool_size = 0

    if len(password) >= 8:
        strength += 1
        if len(password) >= 12:
            strength += 1
            if len(password) >= 16:
                strength += 1
    if any(char.isupper() for char in password):
        strength += 1
        pool_size += 26
    if any(char.islower() for char in password):
        strength += 1
        pool_size += 26
    if any(char.isdigit() for char in password):
        strength += 1
        pool_size += 10
    if any(char in string.punctuation for char in password):
        strength += 1
        pool_size += 32

    common_passwords = {"password", "123456", "123456789", "qwerty", "abc123"}

    if password.lower() in common_passwords:
        strength = 0

    approximate_entropy = len(password) * math.log2(pool_size)

    print("Password entropy (bits):", round(approximate_entropy, 2))

    if approximate_entropy >= 25:
        strength += 1
        if approximate_entropy >= 50:
            strength += 1
            if approximate_entropy >= 75:
                strength += 1
                if approximate_entropy >= 100:
                    strength += 1
                    if approximate_entropy >= 125:
                        strength += 1
                        if approximate_entropy >= 150:
                            strength += 1

    print("Password strength:", strength)