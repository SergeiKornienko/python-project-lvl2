"""Function for determines the difference in files."""


def get_diff(file1, file2):  # noqa: WPS210
    """Determine the difference in files.

    Args:
        file1: dict
        file2: dict

    Returns:
        Return dict with difference.
    """
    changing = {
        "added": {},
        "deleted": {},
        "changed": {},
        "unchanged": {}
    }
    keys = sorted(file1.keys() | file2.keys())

    for key in keys:
        if key not in file2.keys():
            changing["deleted"].update({key: file1[key]})
        elif key not in file1.keys():
            changing["added"].update({key: file2[key]})
        elif file1.get(key) == file2.get(key):
            changing["unchanged"].update({key: file1[key]})
        elif file1.get(key) != file2.get(key) \
                and isinstance(file1.get(key), dict)\
                and isinstance(file2.get(key), dict):
            changing["changed"].update({key: get_diff(file1[key], file2[key])})
        else:
            changing["deleted"].update({key: file1[key]})
            changing["added"].update({key: file2[key]})
    return changing

