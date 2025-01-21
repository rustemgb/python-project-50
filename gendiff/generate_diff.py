from gendiff.gendiff import gendiff
from gendiff.reading_files import reading_files


def generate_diff(file_path1, file_path2):
    file1 = reading_files(file_path1)
    file2 = reading_files(file_path2)
    return gendiff(file1, file2)