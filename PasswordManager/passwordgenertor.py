import random
from Config import minimum_char, letters, symbols, numbers

password_char = []


def gen_password():
    nr_numbers = random.randint(0, minimum_char / 2)
    nr_symbols = random.randint(0, minimum_char / 2 - nr_numbers)
    nr_letters = minimum_char - nr_numbers - nr_symbols
    for n in range(0, nr_letters):
        password_char.append(random.choice(letters))
    for n in range(0, nr_symbols):
        password_char.append(random.choice(symbols))
    for n in range(0, nr_numbers):
        password_char.append(random.choice(numbers))
    random.shuffle(password_char),

    my_password = ""

    for char in password_char:
        my_password += char
    return my_password


def validate_password(password: str) -> bool:
    if len(password) < 12:
        return False
    elif not password_char_comparision(password):
        return False
    else:
        return True


def password_char_comparision(password: str) -> bool:
    has_letter = False
    has_symbol = False
    has_number = False
    for ch in password.split():
        if ch in letters:
            has_letter = True
        if ch in numbers:
            has_number = True
        if ch in symbols:
            has_symbol = True

    if has_number and has_letter and has_symbol:
        return True
    else:
        return False


def get_password():
    new_password = gen_password()
    password_confirmation = input(
        f"Your new password is {new_password}.Do you want yo use it 'Y' or give your own 'N'?)").upper()
    if password_confirmation == 'N':
        new_password = ""
        while not validate_password(new_password):
            print("Please create a 12 char password with Alphabets, Number and Special characters.")
            new_password = input("Please Provide Password.\n")
    return new_password
