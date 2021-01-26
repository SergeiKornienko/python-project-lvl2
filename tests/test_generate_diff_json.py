"""Module of tests generate_diff."""
import json
import pathlib

from gendiff.generate_diff import get_diff
from gendiff.opening_files import get_content

PATH_FILE_DIFF = 'tests/fixtures/diff_file1_file2.json'


def test_gen_diff_json_two_files():
    """Test of function generate_diff with two files."""
    with open('tests/fixtures/expected_file1_file2.json') as infile:
        expected = json.load(infile)
    with open(PATH_FILE_DIFF, 'w') as diff:
        json.dump(
            get_diff(
                *get_content(
                    pathlib.Path('tests/fixtures/file1.json'),
                    pathlib.Path('tests/fixtures/file2.json'),
                ),
            ),
            diff,
        )
    with open(PATH_FILE_DIFF) as diff1:
        assert json.load(diff1) == expected


def test_gen_diff_json_empty_files():
    """Test of function generate_diff with two empty files."""
    with open('tests/fixtures/expected_empty.json') as infile:
        expected = json.load(infile)
    with open(PATH_FILE_DIFF, 'w') as diff:
        json.dump(
            get_diff(
                *get_content(
                    pathlib.Path('tests/fixtures/file_empty.json'),
                    pathlib.Path('tests/fixtures/file_empty2.json'),
                ),
            ),
            diff,
        )
    with open(PATH_FILE_DIFF) as diff1:
        assert json.load(diff1) == expected


def test_gen_diff_json_file_empty():
    """Test of function generate_diff with first file and second empty file."""
    with open('tests/fixtures/expected_file1_empty.json') as infile:
        expected = json.load(infile)
    with open(PATH_FILE_DIFF, 'w') as diff:
        json.dump(
            get_diff(
                *get_content(
                    pathlib.Path('tests/fixtures/file1.json'),
                    pathlib.Path('tests/fixtures/file_empty.json'),
                ),
            ),
            diff,
        )
    with open(PATH_FILE_DIFF) as diff1:
        assert json.load(diff1) == expected


def test_gen_diff_json_empty_file():
    """Test of function generate_diff with first empty file and second file."""
    with open('tests/fixtures/expected_empty_file1.json') as infile:
        expected = json.load(infile)
    with open(PATH_FILE_DIFF, 'w') as diff:
        json.dump(
            get_diff(
                *get_content(
                    pathlib.Path('tests/fixtures/file_empty.json'),
                    pathlib.Path('tests/fixtures/file1.json'),
                ),
            ),
            diff,
        )
    with open(PATH_FILE_DIFF) as diff1:
        assert json.load(diff1) == expected


def test_gen_diff_json_nested():
    """Test of function generate_diff with nested files."""
    with open('tests/fixtures/expected_nested_files.json') as infile:
        expected = json.load(infile)
    with open(PATH_FILE_DIFF, 'w') as diff:
        json.dump(
            get_diff(
                *get_content(
                    pathlib.Path('tests/fixtures/file_nested1.json'),
                    pathlib.Path('tests/fixtures/file_nested2.json'),
                ),
            ),
            diff,
        )
    with open(PATH_FILE_DIFF) as diff1:
        assert json.load(diff1) == expected
