#!/usr/bin/python3


class SwimMixin:
    """Mixin class that adds swimming capability."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that adds flying capability."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
