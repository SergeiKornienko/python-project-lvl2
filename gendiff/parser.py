"""Module for open and parse of a file."""
import json

import yaml


def open_file(file_path):
    """Open file.

    Args:
        file_path: path

    Returns:
        Return content of a file.
    """
    path = str(file_path)
    return open(path, 'r'), path.rsplit('.', 1)[-1]


def parse(infile, suffix):
    """Parse content of a file.

    Args:
        infile: content
        suffix: str

    Returns:
        Return content format dict.
    """
    content_of_file = {}
    if suffix == 'json':
        content_of_file = json.load(infile)
    elif suffix == 'yml':
        content_of_file = yaml.safe_load(infile)
    if not content_of_file:
        return {}
    return content_of_file
