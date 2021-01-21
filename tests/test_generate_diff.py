from gendiff.generate_diff import get_diff


def test_gen_diff1():
    with open('tests/fixtures/expected_file1_file2.txt') as infile1:
        expected = infile1.read()
    with open('tests/fixtures/diff_file1_file2.txt', 'w') as diff:
        diff.write(get_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json'))
    with open('tests/fixtures/diff_file1_file2.txt') as diff:
        assert diff.read() == expected

def test_gen_diff_empty_files():
    with open('tests/fixtures/expected_empty.txt') as infile1:
        expected = infile1.read()
    with open('tests/fixtures/diff_file1_file2.txt', 'w') as diff:
        diff.write(get_diff('tests/fixtures/file_empty.json', 'tests/fixtures/file_empty2.json'))
    with open('tests/fixtures/diff_file1_file2.txt') as diff:
        assert diff.read() == expected

def test_gen_diff2():
    with open('tests/fixtures/expected_file1_empty.txt') as infile1:
        expected = infile1.read()
    with open('tests/fixtures/diff_file1_file2.txt', 'w') as diff:
        diff.write(get_diff('tests/fixtures/file1.json', 'tests/fixtures/file_empty.json'))
    with open('tests/fixtures/diff_file1_file2.txt') as diff:
        assert diff.read() == expected

def test_gen_diff3():
    with open('tests/fixtures/expected_empty_file1.txt') as infile1:
        expected = infile1.read()
    with open('tests/fixtures/diff_file1_file2.txt', 'w') as diff:
        diff.write(get_diff('tests/fixtures/file_empty.json', 'tests/fixtures/file1.json'))
    with open('tests/fixtures/diff_file1_file2.txt') as diff:
        assert diff.read() == expected