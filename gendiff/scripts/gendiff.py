"""Script for launch gendiff."""

from gendiff import engine, generate_diff


def main():
    """Launch gendiff."""
    engine.run(generate_diff.generate_diff)


if __name__ == '__main__':
    main()
