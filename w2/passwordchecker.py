# 1. Bedenk een geheim wachtwoord.
# 2. Zorg dat het wachtwoord 8 tot en met 20 tekens lang is.
# 3. Gebruik minstens één cijfer, zoals 4.
# 4. Gebruik minstens één grote letter, zoals A.
# 5. Gebruik minstens één kleine letter, zoals b.
# 6. Gebruik minstens één teken uit deze rij: *, @, ! of ?.
# 7. Gebruik geen andere tekens.
# 8. Typ je wachtwoord in wanneer daarom wordt gevraagd.
# 9. Is het wachtwoord goed, dan zie je "Valid".
# 10. Is het fout, dan mag je het nog een keer proberen, maximaal drie keer.


def is_valid_password(password):
    digits = set("0123456789")
    uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lowercase = set("abcdefghijklmnopqrstuvwxyz")
    symbols = set("*@!?")
    allowed_characters = digits | uppercase | lowercase | symbols
    password_characters = set(password)

    has_required_length = 8 <= len(password) <= 20
    has_digit = bool(password_characters & digits)
    has_uppercase = bool(password_characters & uppercase)
    has_lowercase = bool(password_characters & lowercase)
    has_symbol = bool(password_characters & symbols)
    has_only_allowed_characters = password_characters <= allowed_characters

    return (
        has_required_length
        and has_digit
        and has_uppercase
        and has_lowercase
        and has_symbol
        and has_only_allowed_characters
    )


def main():
    for _ in range(3):
        password = input("Password: ")
        if is_valid_password(password):
            print("Valid")
            break
    else:
        print("Invalid")


if __name__ == "__main__":
    main()