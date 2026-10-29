import os
import sys


def load_txt_file(file_name):
    file_content = []
    file_names = [file_name.lower()]
    if file_name.lower() == "nlamstdm.txt":
        file_names.append("nlasmtdm.txt")
    script_directory = os.path.dirname(os.path.abspath(__file__))
    search_roots = [sys.path[0], script_directory, os.getcwd()]
    parent_directory = os.path.dirname(script_directory)
    while parent_directory not in search_roots:
        search_roots.append(parent_directory)
        next_parent = os.path.dirname(parent_directory)
        if next_parent == parent_directory:
            break
        parent_directory = next_parent
    search_roots.extend(sys.path)
    file_path = None

    for root in search_roots:
        if not root or not os.path.isdir(root):
            continue
        for name in os.listdir(root):
            if name.lower() in file_names:
                file_path = os.path.join(root, name)
                break
        if file_path is not None:
            break
        for current_root, _directories, files in os.walk(root):
            for name in files:
                if name.lower() in file_names:
                    file_path = os.path.join(current_root, name)
                    break
            if file_path is not None:
                break
        if file_path is not None:
            break

    if file_path is None:
        raise FileNotFoundError(f"Could not find {file_name}")

    with open(file_path, newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            file_content.append(line.split())

    return file_content


def convert_to_dict(data: list) -> dict:
    temperatures = {}

    for row in data:
        month, _day, year, temperature = row
        year_data = temperatures.setdefault(int(year), {})
        year_data.setdefault(int(month), []).append(float(temperature))

    return temperatures


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return round((fahrenheit - 32) * 5 / 9, 4)


def average_temp_per_month(
    temperatures_for_year: dict,
) -> list:
    return [
        (month, sum(temperatures) / len(temperatures))
        for month, temperatures in temperatures_for_year.items()
    ]


def average_temp_per_year(temperatures: dict) -> list:
    return [
        (
            year,
            sum(temperature for values in months.values() for temperature in values)
            / sum(len(values) for values in months.values()),
        )
        for year, months in temperatures.items()
    ]


def _print_warmest_or_coldest_month(temperatures: dict, warmest: bool) -> None:
    year = int(input("Year: "))
    monthly_averages = average_temp_per_month(temperatures[year])
    month, _temperature = (
        max(monthly_averages, key=lambda item: item[1])
        if warmest
        else min(monthly_averages, key=lambda item: item[1])
    )
    month_names = [
        "",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    print(month_names[month])


def main() -> None:
    temperatures = convert_to_dict(load_txt_file("NLAMSTDM.TXT"))
    option = input("Select an option: ")

    if option == "1":
        print(average_temp_per_year(temperatures))
    elif option == "2":
        yearly_averages = average_temp_per_year(temperatures)
        print(list(map(lambda item: (item[0], fahrenheit_to_celsius(item[1])), yearly_averages)))
    elif option == "3":
        yearly_averages = average_temp_per_year(temperatures)
        print(
            (
                max(yearly_averages, key=lambda item: item[1])[0],
                min(yearly_averages, key=lambda item: item[1])[0],
            )
        )
    elif option == "4":
        _print_warmest_or_coldest_month(temperatures, warmest=True)
    elif option == "5":
        _print_warmest_or_coldest_month(temperatures, warmest=False)
    elif option == "6":
        print(
            [
                (
                    year,
                    {
                        month: fahrenheit_to_celsius(temperature)
                        for month, temperature in average_temp_per_month(months)
                    },
                )
                for year, months in temperatures.items()
            ]
        )
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()