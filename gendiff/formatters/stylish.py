"""Module with formatter."""


def make_format(diff, depth=0):
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
            format_diff.append(join_line(depth, '  - ', key, make_value(delete[key], depth+1)))
        if key in add.keys():
            format_diff.append(join_line(depth, '  + ', key, make_value(add[key], depth+1)))
        elif key in unchanged.keys():
            format_diff.append(join_line(depth, '    ', key, make_value(unchanged[key], depth+1)))
        elif key in change.keys():
            format_diff.append(join_line(depth, '    ', key, make_format(change[key], depth=depth+1)))
    print('%%%%%%%%%%%%%%%%%%%%%')
    print(normalization_json_form('\n'.join(['{', *format_diff, ('    ' * (depth) + '}')])))
    return normalization_json_form('\n'.join(['{', *format_diff, ('    ' * (depth) + '}')]))


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


def join_line(depth, indent, key, mean):
    """Join line in dict.

    Args:
        indent: str
        key: str
        mean: str

    Returns:
        Return join line.
    """
    indent_and_key = ''.join([depth * '    ', indent, key, ':'])
    if str(mean) == '':
        return indent_and_key
    return ' '.join([indent_and_key, str(mean)])


def make_value(values, depth):

    def inner(items, count):
        if not isinstance(items, dict):
            return str(items)
        list_values = []
        for key in items.keys():
            list_values.append(''.join([
                '    ' * (count + 1),
                str(key),
                ': ',
                str(inner(
                    items[key],
                    count=count + 1,
                )),
            ]))
        return '\n'.join([
            '{',
            *list_values,
            '{a}{b}'.format(a=('    ' * (count)), b='}'),
        ])
    return inner(values, depth)
