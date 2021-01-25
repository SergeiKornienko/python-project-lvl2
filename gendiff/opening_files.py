"""Function for opening files and get content."""
import json

import yaml


def get_content(file_path1, file_path2):  # noqa: WPS210
    """Get content files.

    Args:
        file_path1: path
        file_path2: path

    Returns:
        Return content files.
    """
    if file_path1.suffix == '.json':
        with open(str(file_path1)) as infile1:
            file1 = json.load(infile1)
        with open(str(file_path2)) as infile2:
            file2 = json.load(infile2)
    elif file_path1.suffix == '.yml':
        with open(str(file_path1)) as infile3:
            file1 = yaml.safe_load(infile3)
        with open(str(file_path2)) as infile4:
            file2 = yaml.safe_load(infile4)
    if file1 is None:
        file1 = {}
    if file2 is None:
        file2 = {}
    return file1, file2
