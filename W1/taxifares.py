# 1. Vraag hoe ver de taxi heeft gereden.
# 2. Begin met 4 euro voor het instappen.
# 3. Kijk hoeveel stukjes van 140 meter de taxi heeft gereden.
# 4. Voor elk stukje betaal je 25 cent.
# 5. Tel alle stukjes geld bij de 4 euro op.
# 6. Vertel hoeveel euro de rit kost.

def calculate_fare(distance):
    """Return the taxi fare for a distance in kilometres."""
    if distance < 0:
        raise ValueError("Distance cannot be negative.")

    distance_in_meters = distance * 1000
    charged_units = int((distance_in_meters + 139) // 140)
    return 4.00 + charged_units * 0.25


def main():
    """Read the travelled distance and print the total fare."""
    distance = float(input("Distance traveled: "))
    total_fare = calculate_fare(distance)
    print(f"Total fare: {total_fare:.2f} EUR")


if __name__ == "__main__":
    main()