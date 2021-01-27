"""Function for determines the difference in files."""
import json

import yaml

from gendiff.formatters import stylish


def generate_diff(file_path1, file_path2, formatter=stylish):
    """Generate difference and formatting.

    Args:
        file_path1: path
        file_path2: path
        formatter: module

    Returns:
        Return formatting difference files.
    """
    suffixes = {file_path1.suffix, file_path2.suffix}
    if len(suffixes) > 1:
        return 'Different format of files!!!'
    if len({'.yml', '.json'} | suffixes) > 2:
        return 'Unsupported format of files!!!'
    return formatter.make_format(
        get_diff(get_content(file_path1), get_content(file_path2)),
    )


def get_content(file_path):  # noqa: WPS210
    """Get content files.

    Args:
        file_path: path

    Returns:
        Return content files.
    """
    if file_path.suffix == '.json':
        with open(str(file_path)) as infile:
            open_file = json.load(infile)
    elif file_path.suffix == '.yml':
        with open(str(file_path)) as infile1:
            open_file = yaml.safe_load(infile1)
    if open_file is None:
        open_file = {}
    return open_file


def get_diff(file1, file2):
    """Determine the difference in files.

    Args:
        file1: dict
        file2: dict

    Returns:
        Return dict with difference.
    """
    changing = {
        'added': {},
        'deleted': {},
        'changed': {},
        'unchanged': {},
    }
    keys = sorted(file1.keys() | file2.keys())

    for key in keys:
        changed = [
            file1.get(key) != file2.get(key),
            isinstance(file1.get(key), dict),
            isinstance(file2.get(key), dict),
        ]
        if key not in file2.keys():
            changing['deleted'].update({key: file1[key]})
        elif key not in file1.keys():
            changing['added'].update({key: file2[key]})
        elif file1.get(key) == file2.get(key):
            changing['unchanged'].update({key: file1[key]})
        elif False not in changed:
            diff_dict = get_diff(file1[key], file2[key])
            changing['changed'].update({key: diff_dict})
        else:
            changing['deleted'].update({key: file1[key]})
            changing['added'].update({key: file2[key]})
    return changing
