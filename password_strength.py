import re


def get_password_strength(password):
    password_strength = 1
    pattern_special_characters = r"\W"
    passwords_special_characters = re.findall(pattern_special_characters,
        password)
    pattern_numbers = r"[0-9]+"
    passwords_numbers = re.findall(pattern_numbers, password)
    if len(password) <= 4:
        password_strength += 1
        return password_strength
    elif len(password) <= 7:
        password_strength += 2
    else:
        password_strength += 3
    if len(passwords_numbers):
        password_strength += 2
    if len(passwords_special_characters):
        password_strength += 2
    if not password.islower():
        password_strength += 1
    if not password.isupper():
        password_strength += 1
    return password_strength


def print_password_strength(password_strength):
    if password_strength <= 2:
        print("{} - Слишком короткий пароль".format(password_strength))
    elif password_strength <= 5:
        print("{} - Слабая надежность пароля".format(password_strength))
    elif password_strength <= 7:
        print("{} - Средняя надежность пароля".format(password_strength))
    else:
        print("{} - Высокая надежность пароля".format(password_strength))


if __name__ == "__main__":
    password = input("Enter a passowrd\n")
    password_strength = get_password_strength(password)
    print_password_strength(password_strength)
