import os

import pytest

from gendiff.differ import generate_diff

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")


def read_fixture(file_name):
    with open(os.path.join(TEST_DATA_DIR, file_name), "r") as file:
        return file.read()


@pytest.mark.parametrize(
    "file1, file2, formatter, file",
    [
        ("file1.json", "file2.json", "stylish", "result_stylish.txt"),
        ("file1.yml", "file2.yml", "stylish", "result_stylish.txt"),
        ("file1.json", "file2.json", "plain", "result_plain.txt"),
        ("file1.yml", "file2.yml", "plain", "result_plain.txt"),
        ("file1.json", "file2.json", "json", "result_json.txt"),
        ("file1.yml", "file2.yml", "json", "result_json.txt"),
    ],
)
def test_generate_diff(file1, file2, formatter, result_file):

    file1_path = os.path.join(TEST_DATA_DIR, file1)
    file2_path = os.path.join(TEST_DATA_DIR, file2)

    correct_result = read_fixture(result_file)
    result = generate_diff(file1_path, file2_path, formatter)

    assert result == correct_result