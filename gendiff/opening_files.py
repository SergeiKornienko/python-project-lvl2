import json
import yaml


def get_content(file_path1, file_path2):
    if file_path1.suffix != file_path2.suffix:
        return 'Different format of files!!!'
    if file_path1.suffix == '.json':
        with open(str(file_path1)) as infile1:
            file1 = json.load(infile1)
        with open(str(file_path2)) as infile2:
            file2 = json.load(infile2)
    elif file_path1.suffix == '.yml':
        with open(str(file_path1)) as infile1:
            file1 = yaml.safe_load(infile1)
        with open(str(file_path2)) as infile2:
            file2 = yaml.safe_load(infile2)
    else:
        return 'Unsupported format of files!!!'
    if file1 is None:
        file1 = {}
    if file2 is None:
        file2 = {}
    return file1, file2
