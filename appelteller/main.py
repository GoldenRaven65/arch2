# testvragen
#hoeveel zakken appels heeft de leverancier nodig
# wat is gewicht van de zakken
#
# vraag voor iedere appel hoeveel kilo die weegt
# voeg de appel toe in de zak
# als de zak boven het minimale gewicht per zak zit ga naar de volgende zak

#stappenplan voor het maken van een UI
# stap 1: maak een input voor het aantal zakken appels
# stap 2: maak een input voor het minimale gewicht van de zakken
# stap 3: maak voor iedere appel een input voor het gewicht
# stap 4: maak een calculator wanneer de zak boven het minimale gewicht per zak zit
# stap 5: ga door naar de volgende zak
# stap 6 ga door tot alle zakken gevuld zijn
#stap 7: print het aantal zakken appels en dat de bestelling klaar is

def positive_number(prompt: str, whole_number: bool = False) -> float:
    while True:
        try:
            entered_value = input(prompt).replace(",", ".")
            value = int(entered_value) if whole_number else float(entered_value)
        except ValueError:
            print("Vul een geldig getal in.")
            continue

        if value <= 0:
            print("Vul een getal groter dan 0 in.")
            continue
        return value


def main() -> None:
    number_of_bags = int(
        positive_number("Hoeveel zakken appels zijn er nodig? ", whole_number=True)
    )
    minimum_weight_per_bag = positive_number(
        "Wat is het minimale gewicht per zak (kg)? "
    )
    for bag_number in range(1, number_of_bags + 1):
        apples_in_bag = 0
        bag_weight = 0.0
        while bag_weight < minimum_weight_per_bag:
            apple_weight = positive_number(
                f"Wat weegt appel {apples_in_bag + 1} voor zak {bag_number} (gram)? "
            ) / 1000
            apples_in_bag += 1
            bag_weight += apple_weight

        print(f"Zak {bag_number}: {apples_in_bag} appels ({bag_weight:.2f} kg)")
    print(f"De bestelling is klaar: {number_of_bags} zakken appels.")


if __name__ == "__main__":
    main()
    