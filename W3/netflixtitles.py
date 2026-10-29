import os
import sys
import csv


def load_csv_file(file_name):
    file_path = file_name
    if not os.path.isfile(file_path):
        file_path = os.path.join(sys.path[0], file_name)

    with open(file_path, newline='', encoding="utf8") as csv_file:
        return list(csv.reader(csv_file, delimiter=","))


def get_headers(file_content):
    """Return the column names from the first row of the CSV content."""
    return file_content[0] if file_content else []


def search_by_type(file_content, show_type):
    """Return rows matching a Netflix content type."""
    return list(filter(lambda row: len(row) > 1 and row[1] == show_type, file_content[1:]))


def search_by_director(file_content, director):
    """Return rows whose director field matches the requested director."""
    return list(filter(lambda row: len(row) > 3 and row[3] == director, file_content[1:]))


def get_directors(file_content):
    """Return the non-empty director fields as a set of unique directors."""
    return set(
        map(
            lambda row: row[3],
            filter(lambda row: len(row) > 3 and row[3] != "", file_content[1:]),
        )
    )


def _director_counts(file_content, director):
    director_titles = search_by_director(file_content, director)
    movies = len(list(filter(lambda row: row[1] == "Movie", director_titles)))
    tv_shows = len(list(filter(lambda row: row[1] == "TV Show", director_titles)))
    return director, movies, tv_shows


def main():
    file_name = sys.argv[1] if len(sys.argv) > 1 else "netflix_titles.csv"
    file_content = load_csv_file(file_name)
    choice = input().strip()

    if choice == "1":
        print(len(search_by_type(file_content, "TV Show")))
    elif choice == "2":
        print(len(search_by_type(file_content, "Movie")))
    elif choice == "3":
        directors = filter(
            lambda director: _director_counts(file_content, director)[1] > 0
            and _director_counts(file_content, director)[2] > 0,
            sorted(get_directors(file_content)),
        )
        print(list(directors))
    elif choice == "4":
        print(
            [
                _director_counts(file_content, director)
                for director in sorted(get_directors(file_content))
            ]
        )


if __name__ == "__main__":
    main()