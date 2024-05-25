#!/usr/bin/python3


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish."""

    def fly(self):
        """Print that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
