"""Script for launch gendiff cli."""
from gendiff.cli import argparser


def main():
    """Launch gendiff cli.

    Returns:
        Return cli.
    """
    return argparser()


if __name__ == '__main__':
    main()
