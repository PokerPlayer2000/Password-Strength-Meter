# Password Strength Meter

A Python tool that evaluates password strength by calculating entropy and generates secure passwords using either random characters or BIP39 word lists.

## Features

- **Password Strength Analysis**: Calculates entropy in bits to determine password strength
- **Entropy-based Security**: Recommends passwords with at least 128 bits of entropy
- **Dual Password Generation Methods**:
  - Random character passwords (letters, numbers, special characters)
  - BIP39 word-based passwords with added complexity
- **Smart Character Set Detection**: Analyzes which character types are used in your password

## How It Works

### Entropy Calculation
The tool calculates password entropy based on:
- Character set size (lowercase, uppercase, digits, special characters)
- Password length
- Formula: `entropy = length × log₂(character_set_size)`

### Password Generation

#### Random Password
- Uses full ASCII character set (letters, numbers, punctuation)
- Minimum length of 16 characters
- Completely random generation for maximum entropy

#### Word-Based Password (BIP39)
- Uses the BIP39 wordlist (2048 words)
- Randomly capitalizes 1-2 letters per word
- Joins words with random special characters
- Inserts 2-4 random digits at random positions
- Example: `aBandon#7fiRe|2gHost&Ocean9`

## Requirements

- Python 3.6+
- `bip39-words.txt` file (included in repository)

## Usage

```bash
python main.py
```

Follow the prompts:
1. Enter your password to check its strength
2. If entropy is below 128 bits, choose to generate:
   - `r` for random character password
   - `w` for word-based password

## Security Recommendations

- **Strong**: ≥ 128 bits of entropy
- **Recommended minimum**: 16 characters for random passwords
- **Word-based**: 4 words with modifications provide good memorability and security

## Files

- `main.py` - Main program file
- `bip39-words.txt` - BIP39 wordlist (2048 words)
- `README.md` - This file

## Example Output

```
Welcome to the Password Strength Meter!
A strong password should have at least 128 bits of entropy.
let's check your password strength.
Enter your password: password123
The entropy of the password is: 57.00 bits
Your password is too weak. Let's make a new one.
Generate a random password (r) or a words-based password (w)? w
Your new password: 7meTal&Rocket#9sUn|