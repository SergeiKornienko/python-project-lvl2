"""Main module of gendiff."""
import argparse
import pathlib
import json
import yaml


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
    print(file_path1.suffix)
    if file_path1.suffix != file_path2.suffix:
        return 'Different format of files!!!'
    if file_path1.suffix == '.json':
        with open(str(file_path1)) as infile1:
            file1 = json.load(infile1)
        with open(str(file_path2)) as infile2:
            file2 = json.load(infile2)
    elif file_path1.suffix == '.yaml':
        with open(str(file_path1)) as infile1:
            file1 = yaml.load(infile1)
        with open(str(file_path2)) as infile2:
            file2 = yaml.load(infile2)
    else:
        return 'Unsuppotred format of files!!!'
    return function(file1, file2)
