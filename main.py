import math
import string
import random

def calculate_entropy(password: str) -> float:
    # define characters
    char_sets = {
        'lower': set(string.ascii_lowercase),
        'upper': set(string.ascii_uppercase),
        'digits': set(string.digits),
        'special': set(string.punctuation)
    }

    # how big the character set should be
    used_char_sets = set()
    password_set = set(password)

    for char_set_name, char_set in char_sets.items():
        if password_set.intersection(char_set):
            used_char_sets.update(char_set)

    char_set_size = len(used_char_sets)

    # calculate entropy
    password_length = len(password)
    if char_set_size == 0:
        return 0

    entropy = password_length * math.log2(char_set_size)
    return entropy

def generate_password(length=20) -> str:
    # chars in password
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate new password
    new_password = ''.join(random.choice(characters) for _ in range(length))
    return new_password

# main thing
password = input("Enter your password: ")
entropy = calculate_entropy(password)
print(f"The entropy of the password is: {entropy:.2f} bits")

if entropy < 100:
    print("Your password is too weak.")
    print("Here is your new password:")
    new_password = generate_password()
    print(new_password)
    print("Goodbye")
else:
    print("Goodbye")
