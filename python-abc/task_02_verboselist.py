#!/usr/bin/python3


class VerboseList(list):
    """Custom list class that provides notifications on operations."""

    def append(self, item):
        """Add item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list with items from iterable and print a notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove item from the list and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index, print a notification."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
