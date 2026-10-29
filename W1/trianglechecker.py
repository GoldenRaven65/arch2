# Stap 1: Lees drie zijden in, gescheiden door spaties.
# Stap 2: Controleer of er precies drie zijden zijn ingevuld.
# Stap 3: Controleer of alle zijden groter zijn dan 0.
# Stap 4: Zoek de langste zijde.
# Stap 5: Tel de andere twee zijden bij elkaar op.
# Stap 6: Controleer of de langste zijde korter is dan de andere twee samen.
# Stap 7: Print of de driehoek mogelijk is.

def check_triangle(side_a, side_b, side_c) -> bool:
    """Return whether three positive lengths can form a triangle."""
    sides = (side_a, side_b, side_c)

    if any(side <= 0 for side in sides):
        return False

    longest_side = max(sides)

    other_sides_total = sum(sides) - longest_side

    return longest_side < other_sides_total


def main() -> None:
    """Read three side lengths and print the result."""
    values = []

    # Lees alle regels, ook als de drie zijden op meerdere regels staan.
    while True:
        try:
            values.extend(input().split())
        except EOFError:
            break

    if len(values) != 3:
        raise ValueError("Exactly three side lengths are required.")

    sides = [float(value) for value in values]

    result = "Possible triangle" if check_triangle(*sides) else "Impossible triangle"

    print(result)


if __name__ == "__main__":
    main()