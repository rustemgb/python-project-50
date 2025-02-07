from gendiff.generator import generator
from gendiff.parser_files import parser_data_from_file
from gendiff.formater.formater import choice_formats


def generate_diff(file_path1, file_path2, formatter="stylish"):
    file1 = parser_data_from_file(file_path1)
    file2 = parser_data_from_file(file_path2)
    diff = generator(file1, file2)
    return choice_formats(diff, formatter)
    