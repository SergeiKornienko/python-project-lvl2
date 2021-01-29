"""Module with formatter stylish."""

TAB = '    '


def make_format(diff, depth=0):
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
    format_diff = []
    for key in keys:
        if key in delete.keys():
            format_diff.append(join_line(
                depth,
                '  - ',
                key,
                format_unchanging(delete[key], depth + 1),
            ))
        if key in add.keys():
            format_diff.append(join_line(
                depth,
                '  + ',
                key,
                format_unchanging(add[key], depth + 1),
            ))
        elif key in unchanged.keys():
            format_diff.append(join_line(
                depth,
                TAB,
                key,
                format_unchanging(unchanged[key], depth + 1),
            ))
        elif key in change.keys():
            format_diff.append(join_line(
                depth,
                TAB,
                key,
                make_format(change[key], depth=depth+1),
            ))
    return normalization_json_form(
        '\n'.join([
            '{',
            *format_diff,
            '{a}{b}'. format(a=TAB * depth, b='}'),
        ]),
    )


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
        depth: int
        indent: str
        key: str
        mean: str

    Returns:
        Return join line.
    """
    indent_and_key = ''.join([depth * TAB, indent, key, ':'])
    if str(mean) == '':
        return indent_and_key
    return ' '.join([indent_and_key, str(mean)])


def format_unchanging(dict_unchanged, depth):
    """Format dict without changing.

    Args:
        dict_unchanged: dict
        depth: int

    Returns:
        Return formatting dict.
    """
    if not isinstance(dict_unchanged, dict):
        return str(dict_unchanged)
    list_values = []
    for key in dict_unchanged.keys():
        list_values.append(''.join([
            TAB * (depth + 1),
            str(key),
            ':',
            ' ',
            str(format_unchanging(
                dict_unchanged[key],
                depth=depth + 1,
            )),
        ]))
    return '\n'.join([
        '{',
        *list_values,
        '{a}{b}'.format(a=(TAB * depth), b='}'),
    ])
