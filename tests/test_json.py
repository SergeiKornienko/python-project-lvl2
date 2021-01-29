"""Module of tests formatter json."""
import pathlib

from gendiff import gendiff


def test_generate_diff_plain_two_simple_files():
    """Test formatter json."""
    with open('tests/fixtures/expected_file1_file2_json.txt') as infile:
        expected = infile.read()
    diff = gendiff.generate_diff(
        pathlib.Path('tests/fixtures/file1.json'),
        pathlib.Path('tests/fixtures/file2.json'),
        formatter='json',
    )
    assert diff == expected


def test_generate_diff_plain_two_nested_files():
    """Test formatter json."""
    with open('tests/fixtures/expected_nested_files_json.txt') as infile:
        expected = infile.read()
    diff = gendiff.generate_diff(
        pathlib.Path('tests/fixtures/file_nested1.yml'),
        pathlib.Path('tests/fixtures/file_nested2.yml'),
        formatter='json',
    )
    assert diff == expected
