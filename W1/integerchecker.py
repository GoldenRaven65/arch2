# Stap 1: Vraag een stukje tekst aan de gebruiker.
# Stap 2: Haal spaties aan het begin en einde weg.
# Stap 3: Kijk of de tekst alleen uit cijfers bestaat.
# Stap 4: Een plus- of minteken mag helemaal vooraan staan.
# Stap 5: Zeg "Valid integer" als de tekst een heel getal is.
# Stap 6: Zeg "Invalid integer" als de tekst geen heel getal is.
# Stap 7: Bij tekst met letters: haal de letters weg en houd de cijfers over.

def is_integer(unchecked: str) -> bool:
    """Return whether unchecked represents a valid integer."""
    value = unchecked.strip()

    if len(value) == 0:
        return False

    if value[0] in "+-":
        value = value[1:]

    return len(value) > 0 and all(character.isdigit() for character in value)


def remove_non_integer(unchecked: str) -> int:
    """Remove letters from unchecked and return the remaining integer."""
    value = unchecked.strip()
    sign = ""

    if value.startswith("+") or value.startswith("-"):
        sign = value[0]
        value = value[1:]

    digits = "".join(character for character in value if character.isdigit())

    if len(digits) == 0:
        raise ValueError("The string does not contain an integer.")

    result = int(sign + digits)
    print(result)
    return result


def main() -> None:
    """Read a string and report whether it represents an integer."""
    unchecked = input()

    if is_integer(unchecked):
        print("Valid integer")
    else:
        print("Invalid integer")


if __name__ == "__main__":
    main()