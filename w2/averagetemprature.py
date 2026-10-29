# 1. We hebben drie dozen met temperaturen: een doos voor 1995,
#    een doos voor 2010 en een doos voor 2020.
# 2. In elke doos staat hoe warm het op elke dag van maart was.
# 3. We zoeken welke temperaturen in twee verschillende dozen hetzelfde zijn.
# 4. Daarna kijken we per jaar wat de hoogste temperatuur was.
# 5. Ten slotte tellen we alle temperaturen van elk jaar bij elkaar op.
# 6. We delen die som door het aantal dagen om het gemiddelde te vinden.
# 7. Het jaar met het hoogste gemiddelde was de warmste maart.


temperatures = (
    (
        "1995",
        "3",
        [
            "47.3", "40.0", "38.3", "36.3", "37.4", "40.3", "41.1", "40.5",
            "41.6", "43.2", "46.2", "45.8", "44.9", "39.4", "40.5", "42.0",
            "46.5", "46.2", "43.3", "41.7", "40.7", "39.6", "44.2", "47.8",
            "45.9", "47.3", "39.8", "35.2", "38.5", "40.5", "47.0",
        ],
    ),
    (
        "2010",
        "3",
        [
            "39.2", "36.7", "35.5", "35.2", "35.8", "33.8", "30.7", "33.2",
            "32.3", "33.3", "37.3", "39.9", "40.8", "42.9", "42.7", "42.6",
            "44.8", "50.3", "52.2", "55.2", "47.2", "45.0", "48.6", "55.0",
            "57.4", "50.9", "48.6", "46.2", "49.6", "50.1", "43.6",
        ],
    ),
    (
        "2020",
        "3",
        [
            "43.2", "41.1", "40.0", "43.6", "42.6", "44.0", "44.0", "47.9",
            "46.6", "50.5", "51.5", "47.7", "44.7", "44.0", "48.9", "45.3",
            "46.6", "49.7", "47.2", "44.8", "41.8", "40.9", "41.0", "42.7",
            "43.4", "44.0", "46.4", "45.5", "40.7", "39.5", "40.6",
        ],
    ),
)

def main():
    days_1995 = set(temperatures[0][2])
    days_2010 = set(temperatures[1][2])
    days_2020 = set(temperatures[2][2])

    print(len(days_1995 & days_2010))
    print(len(days_1995 & days_2020))

    year_with_highest_day = max(
        temperatures,
        key=lambda record: max(map(float, record[2])),
    )[0]
    print(year_with_highest_day)

    warmest_march = max(
        temperatures,
        key=lambda record: sum(map(float, record[2])) / len(record[2]),
    )[0]
    print(warmest_march)


if __name__ == "__main__":
    main()