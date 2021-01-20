"""Function for determines the difference in files."""

import json


def generate_diff(file_path1, file_path2):
    """
    Determines the difference in files.
    :param file_path1: string
    :param file_path2: string
    :return: string
    """
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    keys = sorted(file1.keys() | file2.keys())
    diff = []
    for key in keys:
        if key not in file2.keys():
            diff.append('  - {a}: {b}'.format(a=key, b=file1[key]))
        elif key not in file1.keys():
            diff.append('  + {a}: {b}'.format(a=key, b=file2[key]))
        elif file1.get(key) == file2.get(key):
            diff.append('    {a}: {b}'.format(a=key, b=file2[key]))
        else:
            diff.append(
                '  - {a}: {b}\n  + {a}: {c}'.format(
                    a=key, b=file1[key], c=file2[key]
                )
            )

    return '\n'.join(['{', '\n'.join(diff), '}'])
