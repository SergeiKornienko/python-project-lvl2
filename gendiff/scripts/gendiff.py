"""Script for launch gendiff cli."""
import argparse
import pathlib

from gendiff.gendiff import generate_diff


def main():
    """Launch gendiff cli."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=pathlib.Path)
    parser.add_argument('second_file', type=pathlib.Path)
    parser.add_argument(
        '-f', '--format', default='stylish', help='set format of output',
    )
    args = parser.parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    formatting = args.format
    print(generate_diff(file_path1, file_path2, formatting))


if __name__ == '__main__':
    main()
