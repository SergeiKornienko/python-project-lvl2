"""Function for determines the difference in files."""


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
