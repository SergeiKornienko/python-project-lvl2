"""Module with formatter plain."""

PROPERTY = 'Property'


def render(diff, path=''):
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
    keys = sorted(add.keys() | delete.keys() | change.keys())
    list_diff = []
    for key in keys:
        new_path = key if path == '' else '.'.join([path, key])
        new_path_string = "'{c}'".format(c=new_path)
        if key in delete.keys() & add.keys():
            list_diff.append(' '.join([
                PROPERTY,
                new_path_string,
                'was updated. From',
                convert_for_formatter(delete[key]),
                'to',
                convert_for_formatter(add[key]),
            ]))
        elif key in add.keys() - delete.keys():
            list_diff.append(' '.join([
                PROPERTY,
                new_path_string,
                'was added with value:',
                convert_for_formatter(add[key]),
            ]))
        elif key in delete.keys() - add.keys():
            list_diff.append(' '.join([
                PROPERTY,
                new_path_string,
                'was removed',
            ]))
        elif key in change.keys():
            list_diff.append(render(
                change[key],
                path=new_path,
            ))
    return '\n'.join(list_diff)


def convert_for_formatter(mean):
    """Convert mean.

    Args:
        mean: different

    Returns:
        Return true mean.
    """
    bool_to_json = {'True': 'true', 'False': 'false', 'None': 'null'}
    if str(mean) in bool_to_json.keys():
        return bool_to_json[str(mean)]
    elif isinstance(mean, str):
        return "'{b}'".format(b=mean)
    elif isinstance(mean, dict):
        return '[complex value]'
    return '{b}'.format(b=mean)
