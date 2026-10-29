# Stappenplan voor een kind van 5 jaar:
# 1. Pak een papiertje en schrijf alle letters en tekens van de zin op.
# 2. Kijk naar het eerste teken op het papiertje.
# 3. Kijk of je dit teken al eerder hebt gezien.
# 4. Zet het teken op je lijstje als het er nog niet op staat.
# 5. Ga zo door totdat je alle tekens hebt bekeken.
# 6. Tel hoeveel verschillende tekens er op je lijstje staan.
# 7. Dat getal is het antwoord.


def unique_chars_dict(text: str) -> int:
    """Return the number of unique characters using a dictionary."""
    characters = {}
    for character in text:
        characters[character] = True
    return len(characters)


def unique_chars_set(text: str) -> int:
    """Return the number of unique characters using a set."""
    characters = set()
    for character in text:
        characters.add(character)
    return len(characters)


if __name__ == "__main__":
    text = input()
    print(f"Unique characters: {unique_chars_dict(text)}")