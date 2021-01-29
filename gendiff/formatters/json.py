"""Module with formatter stylish."""

QUOTES = '"'


def make_format(diff, depth=0):
    """Format dict with difference.

    Args:
        diff: dict
        depth: int

    Returns:
        Return formatting difference.
    """
    if isinstance(diff, str):
        return ''.join([QUOTES, str(diff), QUOTES])
    if not isinstance(diff, dict):
        return str(diff)
    if not diff:
        return str(diff)
    list_values = []
    for key in diff.keys():
        list_values.append(''.join([
            '  ' * (depth + 1),
            QUOTES,
            str(key),
            QUOTES,
            ': ',
            str(make_format(
                diff[key],
                depth=depth + 1,
            )),
            ',',
        ]))
    return '\n'.join([
        '{',
        '\n'.join(list_values)[:-1],
        '{a}{b}'.format(a=('  ' * depth), b='}'),
    ])
