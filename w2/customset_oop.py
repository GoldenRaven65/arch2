# 1. We maken een eigen mandje om dingen in te bewaren.
# 2. In het mandje mag hetzelfde ding maar één keer zitten.
# 3. Met "has" vragen we of een ding in het mandje zit.
# 4. Met "add" leggen we een nieuw ding in het mandje.
# 5. Met "remove" halen we een ding uit het mandje.
# 6. Met "union" stoppen we de dingen van twee mandjes samen.
# 7. Met "intersect" houden we alleen de dingen die in beide mandjes zitten.
# 8. Zo gedraagt onze lijst zich een beetje als een echte set.


from __future__ import annotations


class CustomSet:
    def __init__(self, *args):
        """
        Creates a custom set with the given items.
        """
        self.items: list = []

        # For each argument given to the set:
        for item in args:

            # If it's not in the current set:
            if item not in self.items:

                # Add it to the current set
                self.items.append(item)

    def has(self, item) -> bool:
        """
        Returns `True` if the item exists in this set, `False` otherwise.
        """
        return item in self.items

    def add(self, item) -> None:
        """
        Adds the item to the set iff the item isn't in the set already.
        """
        if not self.has(item):
            self.items.append(item)

    def remove(self, item) -> None:
        """
        Removes the item from the set if the item is in the set.
        """
        if self.has(item):
            self.items.remove(item)

    def union(self, other: CustomSet) -> None:
        """
        Gets the union of this instance and another `CustomSet` instance and stores it in this one.
        """
        for item in other.items:
            self.add(item)

    def intersect(self, other: CustomSet) -> None:
        """
        Gets the intersection of this instance and another `CustomSet` instance and stores it in this one.
        """
        self.items = [item for item in self.items if other.has(item)]

    def __len__(self) -> int:
        """
        Returns the length of the custom set when using `len()`.
        """
        return len(self.items)
