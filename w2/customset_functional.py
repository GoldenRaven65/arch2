# 1. We maken een lijstje met dingen, bijvoorbeeld kleuren.
# 2. Een ding mag maar één keer op het lijstje staan.
# 3. Met "has" vragen we: staat dit ding op het lijstje?
# 4. Met "add" zetten we een nieuw ding op het lijstje.
# 5. Staat het ding er al op, dan doen we niets.
# 6. Met "remove" halen we een ding van het lijstje.
# 7. Met "union" maken we één lijstje van twee lijstjes.
# 8. Met "intersect" zoeken we de dingen die op beide lijstjes staan.


def create_set(*args) -> list:
    """
    Creats a custom set with the given items.
    """
    my_set: list = []

    # For each argument given to the set:
    for item in args:

        # If it's not in the current set:
        if item not in my_set:

            # Add it to the current set
            my_set.append(item)

    return my_set


def has(my_set: list, item) -> bool:
    """
    Returns `True` if the item exists in this set, `False` otherwise.
    """
    return item in my_set


def add(my_set: list, item) -> None:
    """
    Adds the item to the set iff the item isn't in the set already.
    """
    if not has(my_set, item):
        my_set.append(item)


def remove(my_set: list, item) -> None:
    """
    Removes the item from the set if the item is in the set.
    """
    if has(my_set, item):
        my_set.remove(item)


def union(my_set: list, other_set: list) -> list:
    """
    Returns a new custom set that contains the union of two sets.
    """
    result = create_set(*my_set)
    for item in other_set:
        add(result, item)
    return result


def intersect(my_set: list, other_set: list) -> list:
    """
    Returns a new custom set that contains the intersection of two sets.
    """
    result = []
    for item in my_set:
        if has(other_set, item):
            add(result, item)
    return result
