# Stap 1: Maak een lijst met alle cadeaus van het kerstlied.
# Stap 2: Maak een lijst met de namen van de twaalf dagen.
# Stap 3: Kies het juiste aantal cadeaus voor de dag.
# Stap 4: Zet de cadeaus in de juiste volgorde.
# Stap 5: Zet komma's tussen de cadeaus.
# Stap 6: Zet "And" voor het laatste cadeau.
# Stap 7: Maak de zin van het vers.
# Stap 8: Herhaal dit voor alle twaalf dagen.

GIFTS_PER_DAY = [
    "A partridge in a pear tree",
    "Two turtledoves",
    "Three French hens",
    "Four calling birds",
    "Five gold rings (five golden rings)",
    "Six geese a-laying",
    "Seven swans a-swimming",
    "Eight maids a-milking",
    "Nine ladies dancing",
    "Ten lords a-leaping",
    "Eleven pipers piping",
    "Twelve drummers drumming",
]

DAY_NAMES = [
    "1st",
    "2nd",
    "3rd",
    "4th",
    "5th",
    "6th",
    "7th",
    "8th",
    "9th",
    "10th",
    "11th",
    "12th",
]


def next_verse(vers_number: int) -> str:
    """Return one verse of The Twelve Days of Christmas."""
    if vers_number < 1 or vers_number > 12:
        raise ValueError("The verse number must be between 1 and 12.")

    gifts = GIFTS_PER_DAY[:vers_number]
    first_gift = gifts[0]

    if vers_number == 1:
        gift_text = first_gift
    else:
        gift_text = ", ".join(reversed(gifts[1:]))
        gift_text += " And " + first_gift

    return (
        f"On the {DAY_NAMES[vers_number - 1]} day of Christmas, "
        f"my true love sent to me {gift_text}"
    )


def main() -> None:
    """Print all twelve verses."""
    for vers_number in range(1, 13):
        print(next_verse(vers_number))


if __name__ == "__main__":
    main()