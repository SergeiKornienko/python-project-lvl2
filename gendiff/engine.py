"""Main module of gendiff."""
import argparse
import pathlib
from gendiff.opening_files import get_content


def run(function):
    """Launch cli.

    Args:
        function: function

    Returns:
        Return result to perform function.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=pathlib.Path)
    parser.add_argument('second_file', type=pathlib.Path)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    suffixes = {file_path1.suffix, file_path2.suffix}
    if len(suffixes) > 1:
        return 'Different format of files!!!'
    if len({'yaml', 'json'} | suffixes) > 2:
        return 'Unsupported format of files!!!'
    return function(*get_content(file_path1, file_path2))
