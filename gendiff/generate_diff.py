"""Function for determines the difference in files."""


def get_diff(file1, file2):  # noqa: WPS210
    """Determine the difference in files.

    Args:
        file1: dict
        file2: dict

    Returns:
        Return string with difference.
    """
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
