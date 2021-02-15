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
    keys = sorted(diff.keys())
    list_diff = []
    for key in keys:
        new_path = key if path == '' else '.'.join([path, key])
        new_path_string = "'{c}'".format(c=new_path)
        if diff[key]['type'] == 'changed':
            list_diff.append(' '.join([
                PROPERTY,
                new_path_string,
                'was updated. From',
                convert_for_formatter(diff[key]['value']),
                'to',
                convert_for_formatter(diff[key]['value_new']),
            ]))
        elif diff[key]['type'] == 'added':
            list_diff.append(' '.join([
                PROPERTY,
                new_path_string,
                'was added with value:',
                convert_for_formatter(diff[key]['value']),
            ]))
        elif diff[key]['type'] == 'deleted':
            list_diff.append(' '.join([
                PROPERTY,
                new_path_string,
                'was removed',
            ]))
        elif diff[key]['type'] == 'nested':
            list_diff.append(render(
                diff[key]['value'],
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
    object_to_json = {'True': 'true', 'False': 'false', 'None': 'null'}
    if str(mean) in object_to_json.keys():
        return object_to_json[str(mean)]
    elif isinstance(mean, str):
        return "'{b}'".format(b=mean)
    elif isinstance(mean, dict):
        return '[complex value]'
    return '{b}'.format(b=mean)
