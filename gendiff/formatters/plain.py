"""Module with formatter plain."""


def make_format(diff, path=''):
    """Format dict with difference.

    Args:
        diff: dict
        depth: int

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
    list_diff = []
    for key in keys:

        if key in change.keys():
            new_path = '.'.join([path, key])
            if new_path.startswith('.'):
                new_path = new_path[1:]
            list_diff.append(make_format(change[key], path=new_path))
        elif key in delete.keys() and key in add.keys():
            list_diff.append(get_string_update(add, delete, key, path))

        elif key in delete.keys():
            new_path = '.'.join([path, key])
            if new_path.startswith('.'):
                new_path = new_path[1:]
            list_diff.append(' '.join([
                'Property',
                "'{a}'".format(a=new_path),
                'was removed'
            ]))
        elif key in add.keys():
            list_diff.append(get_string_add(add, key, path))

    return normalization_json_form('\n'.join(list_diff))


def normalization_json_form(string):
    """Normalize string to json form.

    Args:
        string: str

    Returns:
        Return normalize string.
    """
    string = string.replace("'True'", 'true')
    string = string.replace("'False'", 'false')
    return string.replace("'None'", 'null')


def get_string_add(add, key, path):
    new_path = '.'.join([path, key])
    if new_path.startswith('.'):
        new_path = new_path[1:]
    if isinstance(add[key], dict):
        mean_add = '[complex value]'
    else:
        mean_add = "'{a}'".format(a=add[key])
    return ' '.join([
                'Property',
                "'{a}'".format(a=new_path),
                'was added with value:',
                mean_add,
    ])


def get_string_update(add, delete, key, path):
    new_path = '.'.join([path, key])
    if new_path.startswith('.'):
        new_path = new_path[1:]
    if isinstance(add[key], dict):
        mean_add = '[complex value]'
    else:
        mean_add = "'{a}'".format(a=add[key])
    if isinstance(delete[key], dict):
        mean_del = '[complex value]'
    else:
        mean_del = "'{a}'".format(a=delete[key])
    return ' '.join([
                'Property',
                "'{a}'".format(a=new_path),
                'was updated. From',
                mean_del,
                'to',
                mean_add,
    ])
