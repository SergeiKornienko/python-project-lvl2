"""Module with formatter plain."""

PROPERTY = 'Property'


def make_format(diff, path=''):
    """Format dict with difference.

    Args:
        diff: dict
        path: str

    Returns:
        Return formatting difference.
    """
    add = diff['added']
    delete = diff['deleted']
    change = diff['changed']
    list_diff = []
    for add_key in add.keys() - delete.keys():
        list_diff.append(get_string_add(add, add_key, path))
    for del_key in delete.keys() - add.keys():
        list_diff.append(' '.join([
            PROPERTY,
            "'{a}'".format(a=join_path(path, del_key)),
            'was removed',
        ]))
    for mod_key in delete.keys() & add.keys():
        list_diff.append(get_string_update(add, delete, mod_key, path))
    for change_key in change.keys():
        list_diff.append(make_format(
            change[change_key],
            path=join_path(path, change_key),
        ))
    return normalization_json_form('\n'.join(sorted(list_diff)))


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


def get_string_add(add, key, path):
    """Get string with add items.

    Args:
        add: dict
        key: str
        path: str

    Returns:
        Return string with add items.
    """
    mean_add = check_complex_value(add[key])
    return ' '.join([
        PROPERTY,
        "'{c}'".format(c=join_path(path, key)),
        'was added with value:',
        mean_add,
    ])


def get_string_update(add, delete, key, path):
    """Get string with update items.

    Args:
        add: dict
        delete: dict
        key: str
        path: srt

    Returns:
        Return string with update items.
    """
    mean_add = check_complex_value(add[key])
    mean_del = check_complex_value(delete[key])
    return ' '.join([
        PROPERTY,
        "'{f}'".format(f=join_path(path, key)),
        'was updated. From',
        mean_del,
        'to',
        mean_add,
    ])


def join_path(path, key):
    """Join path to mean.

    Args:
        path: str
        key: str

    Returns:
        Return string with path.
    """
    return key if path == '' else '.'.join([path, key])


def check_complex_value(mean):
    """Check value.

    Args:
        mean: dict

    Returns:
        Return mean value.
    """
    if isinstance(mean, str):
        return "'{b}'".format(b=mean)
    if isinstance(mean, dict):
        return '[complex value]'
    return '{b}'.format(b=mean)
