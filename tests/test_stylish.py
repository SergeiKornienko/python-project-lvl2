"""Module of tests formatter stylish."""
import pathlib

from gendiff import gendiff


def test_generate_diff_stylish_two_simple_files():
    """Test formatters stylish."""
    with open('tests/fixtures/expected_file1_file2.txt') as infile:
        expected = infile.read()
    diff = gendiff.generate_diff(
        pathlib.Path('tests/fixtures/file1.json'),
        pathlib.Path('tests/fixtures/file2.json'),
    )
    assert diff == expected
