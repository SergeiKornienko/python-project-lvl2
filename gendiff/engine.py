"""Main module of gendiff."""
import argparse
import pathlib


def run(function):
    """Launch cli.

    Args:
        function: function
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=pathlib.Path)
    parser.add_argument('second_file', type=pathlib.Path)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file_path1 = str(args.first_file)
    file_path2 = str(args.second_file)
    print(function(file_path1, file_path2))  # noqa:  WPS421
