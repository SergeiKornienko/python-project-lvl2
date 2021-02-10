"""Function for determines the difference in files."""

from gendiff.parser import get_format, parse, read_file
from gendiff.formatters import json as json_format
from gendiff.formatters import plain, stylish

FORMATS = {  # noqa: WPS407
    'stylish': stylish,
    'plain': plain,
    'json': json_format,
}


def generate_diff(file_path1, file_path2, formatter='stylish'):
    """Generate difference and formatting.

    Args:
        file_path1: path
        file_path2: path
        formatter: module

    Returns:
        Return formatting difference files.
    """
    return FORMATS[formatter].render(
        get_diff(
            parse(read_file(file_path1), get_format(file_path1)),
            parse(read_file(file_path2), get_format(file_path2)),
        ),
    )


def get_diff(file1, file2):
    """Determine the difference in files.

    Args:
        file1: dict
        file2: dict

    Returns:
        Return dict with difference.
    """
    tree_diff = {}
    keys = file1.keys() | file2.keys()
    for key in keys:
        noda = {}
        value1 = file1.get(key)
        value2 = file2.get(key)
        if key not in file2.keys():
            noda['type'] = 'deleted'
            noda['value'] = value1
        elif key not in file1.keys():
            noda['type'] = 'added'
            noda['value'] = value2
        elif value1 == value2:
            noda['type'] = 'unchanged'
            noda['value'] = value1
        elif all([
            value1 != value2,
            isinstance(value1, dict),
            isinstance(value2, dict),
        ]):
            noda['value'] = get_diff(value1, value2)
            noda['type'] = 'default'
        else:
            noda['type'] = 'changed'
            noda['value'] = value1
            noda['value_new'] = value2
        tree_diff[key] = noda
    return tree_diff
