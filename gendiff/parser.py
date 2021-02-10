"""Module for open and parse of a file."""
import json

import yaml


def get_format(file_path):
    """Get format of file.

    Args:
        file_path: path

    Returns:
        Return suffix of file.
    """
    return str(file_path).rsplit('.', 1)[-1]


def read_file(file_path):
    """Open file.

    Args:
        file_path: path

    Returns:
        Return content of a file.
    """
    path = str(file_path)
    with open(path, 'r') as infile:
        content = infile.read()
    return content


def parse(content, suffix):
    """Parse content of a file.

    Args:
        content: content
        suffix: str

    Returns:
        Return content format dict.
    """
    content_of_file = {}
    if suffix == 'json':
        content_of_file = json.loads(content)
    elif suffix == 'yml':
        content_of_file = yaml.safe_load(content)
    if not content_of_file:
        return {}
    return content_of_file
