from gendiff.generator import generator
from gendiff.parser_files import parser_data_from_file


def generate_diff(file_path1, file_path2):
    file1 = parser_data_from_file(file_path1)
    file2 = parser_data_from_file(file_path2)
    return generator(file1, file2)