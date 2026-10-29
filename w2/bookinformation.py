# Stappenplan voor een kind van 5 jaar:
# 1. Maak een leeg lijstje voor je boeken.
# 2. Kies of je een boek wilt toevoegen, zoeken of stoppen.
# 3. Om een boek toe te voegen, schrijf je de titel, schrijver,
#    uitgever en datum op.
# 4. Kijk eerst of de titel al op je lijstje staat.
# 5. Staat de titel er nog niet op? Zet het boek dan op je lijstje.
# 6. Om een boek te zoeken, typ je een woord dat je kent.
# 7. Kijk of het woord in de titel, schrijver of uitgever staat.
# 8. Zeg "gevonden" als je het boek ziet.
# 9. Als je klaar bent, druk je alle boeken van je lijstje af.


def search_book(books, term):
    """Return whether term occurs in a title, author, or publisher."""
    term = term.lower()
    return any(
        term in book[field].lower()
        for book in books
        for field in ("title", "author", "publisher")
    )


def main():
    books = []

    while True:
        choice = input("[A] Add book[S] Search book[E] Exit (and print)\n").strip().upper()

        if choice == "A":
            details = input("Book details: ").split(",")
            if len(details) != 4:
                print("Invalid book details")
                continue

            title, author, publisher, pub_date = (
                detail.strip() for detail in details
            )
            if any(book["title"].lower() == title.lower() for book in books):
                print("Book already exists")
                continue

            books.append(
                {
                    "title": title,
                    "author": author,
                    "publisher": publisher,
                    "pub_date": pub_date,
                }
            )
            print("Book has been added")

        elif choice == "S":
            term = input("Search term: ").strip()
            if search_book(books, term):
                print(f"Found a book for: {term}")
            else:
                print(f"No book found for: {term}")

        elif choice == "E":
            for book in books:
                print(book, end="")
            break


if __name__ == "__main__":
    main()