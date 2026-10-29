# Stap 1: Lees alle pakketregels uit het CSV-bestand.
# Stap 2: Controleer de namen, cijfers, afmetingen en postcode.
# Stap 3: Zet goede regels bij de geldige regels.
# Stap 4: Zet foute regels bij de corrupte regels met de reden erbij.
# Stap 5: Bereken voor elk goed pakket het volume.
# Stap 6: Maak een adres van de straat en het huisnummer.
# Stap 7: Print de geldige regels en de georganiseerde pakketten.
# Stap 8: Print daarna de corrupte regels met hun fouten.

valid_lines = []
corrupt_lines = []

def read_csv_as_string_list(filepath: str) -> list:
    """
    Reads a CSV file and returns a list of strings,
    each representing a row (excluding the first row which is the header).
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines[1:]:
        cleaned_line = line.strip()
        cleaned_lines.append(cleaned_line)
    return cleaned_lines

def is_valid_postcode(postcode: str) -> bool:
    """
    Validates Dutch postcode format using basic loops and string checks.
    Format: 4 digits followed by 2 uppercase letters (optional space allowed).
    """
    if len(postcode) == 7 and postcode[4] == " ":
        postcode = postcode[:4] + postcode[5:]

    return (
        len(postcode) == 6
        and postcode[:4].isdigit()
        and postcode[4:].isalpha()
        and postcode[4:].isupper()
    )

def is_positive(value: str) -> bool:
    """
    Checks if the value is a positive non-zero float.
    """    
    try:
        return float(value) > 0
    except ValueError:
        return False


def is_valid_name(name: str) -> bool:
    """Return whether a name contains only letters and spaces."""
    return bool(name.strip()) and all(
        character.isalpha() or character == " "
        for character in name
    )


def filter_data(rows: list) -> None:
    """
    Processes the rows extracted from the input file, checks all the requested validity conditions 
    and fills valid_lines and corrupt_lines.
    """
    valid_lines.clear()
    corrupt_lines.clear()

    for row in rows:
        values = row.split(",")
        issues = []

        if len(values) != 11:
            corrupt_lines.append((row, ["Invalid number of values"]))
            continue

        sender_firstname, sender_lastname = values[0], values[1]
        receiver_firstname, receiver_lastname = values[2], values[3]
        weight, length, width, height = values[4:8]
        street, house_number, postcode = values[8:11]

        if not is_valid_name(sender_firstname) or not is_valid_name(sender_lastname):
            issues.append("Invalid sender name")
        if not is_valid_name(receiver_firstname) or not is_valid_name(receiver_lastname):
            issues.append("Invalid receiver name")
        if not is_positive(weight):
            issues.append("Invalid weight")
        if not is_positive(length) or not is_positive(width) or not is_positive(height):
            issues.append("Invalid dimensions")
        if not street.strip() or not house_number.strip():
            issues.append("Invalid address")
        if not is_valid_postcode(postcode):
            issues.append("Invalid postcode")

        if issues:
            corrupt_lines.append((row, issues))
        else:
            valid_lines.append(row)

def organise_packages_by_postcode(valid_rows)->None:
    """
    For each valid package row:
    - Calculates volume: Length * Width * Height
    - Creates a tuple: (postcode, street + house number, volume)
    - Prints all triples for reporting
    """
    package_groups = []

    for row in valid_rows:
        values = row.split(",")
        postcode = values[10].replace(" ", "")
        address = f"{values[8]} {values[9]}"
        volume = float(values[5]) * float(values[6]) * float(values[7])
        package_groups.append((postcode, address, volume))

    print("### ORGANISED PACKAGES BY POSTCODE ###")
    for postcode, address, volume in package_groups:
        print(
            f"Postcode: {postcode}, Address: {address}, "
            f"Volume: {volume:.2f}"
        )

def report_corrupt_data()->None:
    """
    Prints all corrupt rows with their issues.
    """
    print("### CORRUPT LINES ###")
    for row, issues in corrupt_lines:
        print(f"{row}  -->  {'; '.join(issues)}")


def main():
    # Define the file path relative to the script
    filename = "packages.csv"  # Replace with your actual CSV filename
    # Step 1: Read and clean the data
    rows = read_csv_as_string_list(filename)
    # Step 2: Polish and validate the data
    filter_data(rows)
    print("### VALID LINES ###")
    for row in valid_lines:
        print(row)
    # Step 3: Report valid lines and group packages
    organise_packages_by_postcode(valid_lines)
    # Step 4: Report corrupt lines
    report_corrupt_data()

if __name__ == "__main__":
    main()