"""Module with formatter."""


def make_format(diff):
    """Format dict with difference.

    Args:
        diff: dict

    Returns:
        Return formatting difference.
    """
    add = diff['added']
    delete = diff['deleted']
    change = diff['changed']
    unchanged = diff['unchanged']
    keys = sorted(
        add.keys() |
        delete.keys() |
        change.keys() |
        unchanged.keys(),
    )
    format_diff = []
    for key in keys:
        if key in delete.keys():
            format_diff.append(join_line('  - ', key, delete[key]))
        if key in add.keys():
            format_diff.append(join_line('  + ', key, add[key]))
        elif key in unchanged.keys():
            format_diff.append(join_line('    ', key, unchanged[key]))
        elif key in change.keys():
            format_diff.append(join_line('    ', key, change[key]))
    return normalization_json_form('\n'.join(['{', *format_diff, '}']))


def normalization_json_form(string):
    """Normalize string to json form.

    Args:
        string: str

    Returns:
        Return normalize string.
    """
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    return string.replace('None', 'null')


def join_line(indent, key, mean):
    """Join line in dict.

    Args:
        indent: str
        key: str
        mean: str

    Returns:
        Return join line.
    """
    return ''.join([indent, key, ': ', str(mean)])
