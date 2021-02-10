"""Module of tests get_diff."""
import json
import pathlib
import pytest

from gendiff.gendiff import get_diff
from gendiff.parser import get_format, parse, read_file

PATH_FILE_DIFF = 'tests/fixtures/diff_file1_file2.json'


@pytest.mark.parametrize('file1,file2,expected_file', [
    (
     'tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/expected_file1_file2.json',
     ),
    (
     'tests/fixtures/file_empty.json',
     'tests/fixtures/file_empty2.json',
     'tests/fixtures/expected_empty.json',
    ),
    (
     'tests/fixtures/file1.json',
     'tests/fixtures/file_empty.json',
     'tests/fixtures/expected_file1_empty.json',
    ),
    (
     'tests/fixtures/file_empty.json',
     'tests/fixtures/file1.json',
     'tests/fixtures/expected_empty_file1.json',
    ),
    (
     'tests/fixtures/file_nested1.json',
     'tests/fixtures/file_nested2.json',
     'tests/fixtures/expected_nested_files.json',
    ),
    (
     'tests/fixtures/file1.yml',
     'tests/fixtures/file2.yml',
     'tests/fixtures/expected_file1_file2.json',
    ),
    (
     'tests/fixtures/file_empty.yml',
     'tests/fixtures/file_empty2.yml',
     'tests/fixtures/expected_empty.json',
    ),
    (
     'tests/fixtures/file1.yml',
     'tests/fixtures/file_empty.yml',
     'tests/fixtures/expected_file1_empty.json',
    ),
    (
     'tests/fixtures/file_empty.yml',
     'tests/fixtures/file1.yml',
     'tests/fixtures/expected_empty_file1.json',
    ),
    (
     'tests/fixtures/file_nested1.yml',
     'tests/fixtures/file_nested2.yml',
     'tests/fixtures/expected_nested_files.json',
    ),
])
def test_get_diff(file1, file2, expected_file):
    """Test of function get_diff with two files."""
    expected = parse(
        read_file(pathlib.Path(expected_file)),
        get_format(pathlib.Path(expected_file)),
    )
    with open(PATH_FILE_DIFF, 'w') as diff:
        json.dump(
            get_diff(
                parse(
                    read_file(pathlib.Path(file1)),
                    get_format(pathlib.Path(file1)),
                ),
                parse(
                    read_file(pathlib.Path(file2)),
                    get_format(pathlib.Path(file2)),
                ),
            ),
            diff,
        )
    with open(PATH_FILE_DIFF) as diff1:
        assert json.load(diff1) == expected
