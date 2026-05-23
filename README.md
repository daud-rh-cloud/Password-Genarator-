# Password-Genarator

A command-line password generator built while learning Python.

## What it does

- Asks how long you want the password to be
- Lets you choose which character types to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Symbols (!@#$%...)
- Generates a random password based on your choices

## How to run

```bash
python main.py
```

## What I learned

- `import random` and `import string`
- `random.choices()` and the `k=` parameter
- `''.join()` to convert a list into a string
- `string.ascii_uppercase`, `string.digits`, `string.punctuation`
- While loops and user input validation
