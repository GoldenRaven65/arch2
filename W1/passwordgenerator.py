# Stap 1: Kies een willekeurig aantal tekens tussen 7 en 10.
# Stap 2: Kies voor elk teken een willekeurig nummer tussen 33 en 126.
# Stap 3: Maak van elk nummer een teken.
# Stap 4: Plak alle tekens achter elkaar.
# Stap 5: Geef het nieuwe wachtwoord terug.
# Stap 6: Laat het wachtwoord op het scherm zien.

import random


def generate_random_password() -> str:
    """Generate a password with random printable ASCII characters."""
    password_length = random.randint(7, 10)
    password = ""

    for _ in range(password_length):
        ascii_number = random.randint(33, 126)
        password += chr(ascii_number)

    return password


def main() -> None:
    """Generate and print a random password."""
    print(generate_random_password())


if __name__ == "__main__":
    main()