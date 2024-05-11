#!/usr/bin/python3
import sys


def main():
    total = 0
    for num in sys.argv[1:]:
        total += int(num)
    print(total)


if __name__ == "__main__":
    main()
