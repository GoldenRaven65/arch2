# Zo werkt dit programma, net als een vriendenboekje:
# 1. We bewaren de namen van alle kinderen in een groot vriendenboek.
# 2. Bij iedere naam schrijven we op welke andere kinderen vrienden zijn.
# 3. Bij het starten leest het programma dit vriendenboek uit een JSON-bestand.
# 4. De computer maakt van iedere vriendenlijst een set, zodat namen niet dubbel
#    worden opgeslagen.
# 5. Met L laten we alle namen netjes op alfabet zien.
# 6. Met S vragen we de naam van een kind en laten we diens directe vrienden zien.
# 7. Met R kijken we via de vrienden naar nieuwe mogelijke vrienden.
# 8. Een bestaande vriend of het kind zelf wordt nooit als nieuwe vriend voorgesteld.
# 9. We tellen hoe vaak een nieuwe naam via gezamenlijke vrienden voorkomt.
# 10. Met Q stoppen we het programma.

import json


def load_social_network(filename):
    """
    Loads the social network from a JSON file and returns a dictionary
    where keys are usernames and values are sets of direct friends.
    """
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            network = {}
            for user, friends in data.items():
                network[user] = set(friends)
            return network
    except FileNotFoundError:
        print("Error: JSON file not found.")
        return {}


def list_users(network):
    """
    Lists all users in the network, sorted alphabetically.
    """
    print(", ".join(sorted(network)))


def show_friends(user, network):
    """
    Shows direct friends of the specified user.
    If user is not found, prints an error message: Error: User not found.
    """
    if user not in network:
        print("Error: User not found.")
        return

    friends = sorted(network[user])
    if not friends:
        print("User has no friends.")
        return

    print(", ".join(friends))


def recommend_friends(user, network):
    """
    Recommends friends of friends for a user, excluding their current friends and self.
    Displays mutual friend count for each recommendation.
    """
    if user not in network:
        print("Error: User not found.")
        return

    direct_friends = network[user]
    mutual_friend_counts = {}

    for friend in direct_friends:
        for friend_of_friend in network.get(friend, set()):
            if friend_of_friend != user and friend_of_friend not in direct_friends:
                mutual_friend_counts[friend_of_friend] = (
                    mutual_friend_counts.get(friend_of_friend, 0) + 1
                )

    if not mutual_friend_counts:
        print("No Recommendation.")
        return

    print(f"Recommended friends for {user}:")
    for recommendation in sorted(mutual_friend_counts):
        count = mutual_friend_counts[recommendation]
        print(f"- {recommendation} ({count} mutual friends)")


def main():
    filename = "friends.json"
    network = load_social_network(filename)

    while True:
        print("[L] List users (sorted alphabetically)")
        print("[S] Show friends of user (sorted alphabetically)")
        print("[R] Recommend friends (sorted alphabetically)")
        print("[Q] Quit program")

        choice = input().strip().upper()

        if choice == "L":
            list_users(network)
        elif choice == "S":
            user = input("Enter username: ")
            show_friends(user, network)
        elif choice == "R":
            user = input("Enter username: ")
            recommend_friends(user, network)
        elif choice == "Q":
            break


if __name__ == "__main__":
    main()