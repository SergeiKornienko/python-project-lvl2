"""Module of tests generate_diff."""
import pathlib

from gendiff.generate_diff import get_diff
from gendiff.opening_files import get_content

PATH_FILE_DIFF = 'tests/fixtures/diff_file1_file2.txt'


def test_gen_diff_yaml_two_files():
    """Test of function generate_diff with two files."""
    with open('tests/fixtures/expected_file1_file2.txt') as infile:
        expected = infile.read()
    with open(PATH_FILE_DIFF, 'w') as diff:
        diff.write(get_diff(*get_content(
            pathlib.Path('tests/fixtures/file1.yml'),
            pathlib.Path('tests/fixtures/file2.yml'),
        )))
    with open(PATH_FILE_DIFF) as diff1:
        assert diff1.read() == expected


def test_gen_diff_yaml_empty_files():
    """Test of function generate_diff with two empty files."""
    with open('tests/fixtures/expected_empty.txt') as infile:
        expected = infile.read()
    with open(PATH_FILE_DIFF, 'w') as diff:
        diff.write(get_diff(*get_content(
            pathlib.Path('tests/fixtures/file_empty.yml'),
            pathlib.Path('tests/fixtures/file_empty2.yml'),
        )))
    with open(PATH_FILE_DIFF) as diff1:
        assert diff1.read() == expected


def test_gen_diff_yaml_file_empty():
    """Test of function generate_diff with first file and second empty file."""
    with open('tests/fixtures/expected_file1_empty.txt') as infile:
        expected = infile.read()
    with open(PATH_FILE_DIFF, 'w') as diff:
        diff.write(get_diff(*get_content(
            pathlib.Path('tests/fixtures/file1.yml'),
            pathlib.Path('tests/fixtures/file_empty.yml'),
        )))
    with open(PATH_FILE_DIFF) as diff1:
        assert diff1.read() == expected


def test_gen_diff_yaml_empty_file():
    """Test of function generate_diff with first empty file and second file."""
    with open('tests/fixtures/expected_empty_file1.txt') as infile:
        expected = infile.read()
    with open(PATH_FILE_DIFF, 'w') as diff:
        diff.write(get_diff(*get_content(
            pathlib.Path('tests/fixtures/file_empty.yml'),
            pathlib.Path('tests/fixtures/file1.yml'),
        )))
    with open(PATH_FILE_DIFF) as diff1:
        assert diff1.read() == expected
