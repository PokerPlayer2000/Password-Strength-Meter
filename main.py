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

def generate_random_password(length) -> str:
    # chars in password
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate new password
    new_password = ''.join(random.choice(characters) for _ in range(length))
    return new_password

def generate_words_password(num_words=4) -> str:
    # read word list from file
    with open('bip39-words.txt', 'r') as file:
        word_list = [line.strip() for line in file.readlines()]

    # generate words
    selected_words = [random.choice(word_list) for _ in range(num_words)]
    
    # randomly capitalize some letters in each word
    modified_words = []
    for word in selected_words:
        chars = list(word)
        # randomly capitalize 1-2 letters per word
        num_caps = random.randint(1, min(2, len(word)))
        positions = random.sample(range(len(word)), num_caps)
        for pos in positions:
            chars[pos] = chars[pos].upper()
        modified_words.append(''.join(chars))
    
    # join words with random special characters (no spaces)
    special_chars = '!@#$%^&*()-_+=[]{}|;:,.<>?/'
    separators = [random.choice(special_chars) for _ in range(num_words - 1)]
    
    # combine words with separators
    password_parts = []
    for i, word in enumerate(modified_words):
        password_parts.append(word)
        if i < len(separators):
            password_parts.append(separators[i])
    
    # add random numbers at random positions
    num_digits = random.randint(2, 4)
    for _ in range(num_digits):
        digit = str(random.randint(0, 9))
        position = random.randint(0, len(password_parts))
        password_parts.insert(position, digit)
    
    # join everything together
    new_password = ''.join(password_parts)
    return new_password

def make_password():
    choice = input("Generate a random password (r) or a words-based password (w)? ").strip().lower()
    if choice == 'w':
        new_password = generate_words_password()
        print(f"Your new password: {new_password}")
    else:
        length = int(input("Enter desired password length (minimum 16): "))
        if length < 16:
            length = 16
            print("Length set to minimum of 16.")
        new_password = generate_random_password(length)
        print(f"Your new password: {new_password}")


# welcome message
print("Welcome to the Password Strength Meter!")
print("A strong password should have at least 128 bits of entropy.")
print("let's check your password strength.")

# main thing
password = input("Enter your password: ")
entropy = calculate_entropy(password)
print(f"The entropy of the password is: {entropy:.2f} bits")

if entropy < 128:
    print("Your password is too weak. Let's make a new one.")
    make_password
else:
    print("Your password is strong enough.")

print("Goodbye")
