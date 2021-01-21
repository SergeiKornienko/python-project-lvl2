"""Function for determines the difference in files."""
import json


def get_diff(file_path1, file_path2):  # noqa: WPS210
    """Determine the difference in files.

    Args:
        file_path1: str
        file_path2: str

    Returns:
        Return string with difference.
    """
    with open(file_path1) as infile1:
        file1 = json.load(infile1)
    with open(file_path2) as infile2:
        file2 = json.load(infile2)
    keys = sorted(file1.keys() | file2.keys())

    def inner(key):  # noqa: WPS430
        if key not in file2.keys():
            return '  - {a}: {b}'.format(a=key, b=file1[key])
        elif key not in file1.keys():
            return '  + {a}: {b}'.format(a=key, b=file2[key])
        elif file1.get(key) == file2.get(key):
            return '    {a}: {b}'.format(a=key, b=file2[key])
        return '  - {a}: {b}\n  + {a}: {c}'.format(
            a=key, b=file1[key], c=file2[key],
        )
    diff = '\n'.join(list(map(inner, keys)))
    return '\n'.join(['{', diff, '}']).lower()
