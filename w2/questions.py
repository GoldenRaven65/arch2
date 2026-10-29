students = [
    {"number": "1151237", "firstname": "Merijn", "lastname": "Arts", "day": 3, "month": 5, "year": 2006},
    {"number": "1147596", "firstname": "Jasper", "lastname": "van Velzen", "day": 12, "month": 2, "year": 2009},
    {"number": "1048872", "firstname": "Zeyno", "lastname": "Işık", "day": 23, "month": 11, "year": 2002},
    {"number": "1142052", "firstname": "Arda", "lastname": "Kuzucu", "day": 7, "month": 3, "year": 2006},
    {"number": "1153388", "firstname": "Furkan", "lastname": "Kara", "day": 19, "month": 6, "year": 2002},
    {"number": "1144740", "firstname": "Jaïr", "lastname": "Maduro", "day": 19, "month": 9, "year": 2006},
    {"number": "1146425", "firstname": "Zakariye", "lastname": "Hassan", "day": 23, "month": 7, "year": 2008},
    {"number": "1150431", "firstname": "Jerry", "lastname": "Nguyen", "day": 9, "month": 10, "year": 2003},
    {"number": "1112571", "firstname": "Maram", "lastname": "Al Halabi", "day": 9, "month": 2, "year": 1996},
    {"number": "1131018", "firstname": "Yusuf", "lastname": "Eryiğit", "day": 30, "month": 4, "year": 2005},
    {"number": "1143023", "firstname": "Hielke", "lastname": "Scherrenburg", "day": 17, "month": 5, "year": 2007},
    {"number": "1103385", "firstname": "Nora", "lastname": "Chara", "day": 20, "month": 10, "year": 2006},
    {"number": "1144919", "firstname": "Yousif", "lastname": "Saoor", "day": 2, "month": 5, "year": 2004},
    {"number": "1136823", "firstname": "Martijn", "lastname": "Wissenburg", "day": 22, "month": 10, "year": 2007},
    {"number": "1142733", "firstname": "Lien", "lastname": "Abo Alzien", "day": 14, "month": 5, "year": 2009},
    {"number": "1145092", "firstname": "Aya", "lastname": "Yekhlef", "day": 28, "month": 1, "year": 2004},
    {"number": "1134812", "firstname": "Emad", "lastname": "Pahenda", "day": 14, "month": 12, "year": 2006},
    {"number": "1140803", "firstname": "Dico", "lastname": "Schmitz", "day": 27, "month": 8, "year": 2009},
    {"number": "1119308", "firstname": "Délano", "lastname": "Kalkhoven", "day": 10, "month": 8, "year": 2007},
    {"number": "1145153", "firstname": "Alperen", "lastname": "Gülseren", "day": 15, "month": 4, "year": 2008},
    {"number": "1136997", "firstname": "Yarik", "lastname": "Starchenko", "day": 5, "month": 11, "year": 2008},
]


def print_people(students):
    print(f'{len(students)} people:')
    for student in students:
        number_and_name = f"{student['number']:7s} {student['firstname']:8s} {student['lastname']:12s}"
        date_of_birth = f"{student['day']:02d}-{student['month']:02d}-{student['year']:4d}"
        print(number_and_name, date_of_birth)
    print("-" * 40)

print_people(students)

# 1. Sorteer de lijst met studenten
#    Tip: gebruik de functie `sort()`


# 2. Waarom lukt dat niet?
# omdat je niet weet op wat je moet sorteren

# 3. Sorteer de studenten op nummer en print de lijst
#    Tip 1: maak eerst een functie `number(student: dict) -> str` die alleen het nummer van een student teruggeeft
#    Tip 2: geef die functie mee als waarde voor de parameter `key`
# def number(student: dict) -> str:
#     return student['number']

# #print (number(students[0]))
# students.sort(key=number)
# print_people(students)d
# 4. Sorteer de studenten op nummer en print de lijst
#    Tip: gebruik een anonieme functie (een `lambda`)
# students.sort(key=lambda student: student['number'])
# print_people(students)

# 5. Sorteer de studenten op voornaam
# students.sort(key=lambda student: student['firstname'])
# print_people(students)

# 6. Sorteer de studenten op verjaardag (een verjaardagskalender)
# students.sort(key=lambda student: (student['year'], student['month'], student['day']))
# print_people(students)

# 7. Maak een lijst met studenten die in jarig zijn tijdens BaseCamp (september t/m januari)
#    Tip: gebruik de functie `filter()` met een anonieme functie
# students_birthday_basecamp = list(filter(lambda student: student['month'] in [9, 10, 11, 12, 1], students))
# print_people(students_birthday_basecamp)

# # 8. Maak een lijst met alle voornamen
# #    Tip: gebruik de functie `map()` met een anonieme functie
# student_firstnames = list(map(lambda student: student['firstname'], students))
# print(student_firstnames)

# # 9. Maak een lijst met alle voornamen
# #     Tip: gebruik een list comprehension
# firstnames = [student['firstname'] for student in students]
# print(firstnames)   

# 10. Maak een lijst studenten die jarig zijn tijdens BaseCamp (september t/m januari)
#     Tip: gebruik een list comprehension
students_birthday_basecamp = [student for student in students if student['month'] in [9, 10, 11, 12, 1]]
print_people(students_birthday_basecamp)


# 11. Schrijf een functie `my_filter(func, iterable)` die hetzelfde doet als de functie `filter()`
#     Optioneel


# 12. Schrijf een functie `my_map(func, iterable)` die hetzelfde doet als de functie `map()`
#     Optioneel

# 13. Schrijf een functie `my_reduce(func, iterable, initial)` die hetzelfde doet als de functie `reduce()` in `functools`
#     Optioneel
