import re
import getpass


def get_password_strength(password):
    min_length = 4
    average_length = 7
    password_strength = 1
    pattern_special_characters = r"\W"
    passwords_special_characters = re.search(pattern_special_characters,
        password)
    pattern_digits = r"[0-9]+"
    passwords_digits = re.search(pattern_digits, password)
    if len(password) <= min_length:
        password_strength += 1
        return password_strength
    elif len(password) <= average_length:
        password_strength += 2
    else:
        password_strength += 3
    if bool(passwords_digits):
        password_strength += 2
    if bool(passwords_special_characters):
        password_strength += 2
    if not password.islower() and not password.isupper():
        password_strength += 2
    return password_strength


def print_password_strength(password_strength):
    short_pass_strength = 2
    low_security_pass_strenght = 5
    average_security_pass_strength = 7
    if password_strength <= short_pass_strength:
        print("{} - Слишком короткий пароль".format(password_strength))
    elif password_strength <= low_security_pass_strenght:
        print("{} - Слабая надежность пароля".format(password_strength))
    elif password_strength <= average_security_pass_strength:
        print("{} - Средняя надежность пароля".format(password_strength))
    else:
        print("{} - Высокая надежность пароля".format(password_strength))


if __name__ == "__main__":
    password = getpass.getpass("Введите пароль\n")
    password_strength = get_password_strength(password)
    print_password_strength(password_strength)
