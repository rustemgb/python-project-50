import os

import pytest

from gendiff.generate_diff import generate_diff

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")


def read_fixture(file_name):
    with open(os.path.join(TEST_DATA_DIR, file_name), "r") as file:
        return file.read()


@pytest.mark.parametrize(
    "file1, file2, format, result",
    [
        ("file1.json", "file2.json", "stylish", "result_stylish.txt"),
        ("file1.yaml", "file2.yaml", "stylish", "result_stylish.txt"),
        ("file1.json", "file2.json", "plain", "result_plain.txt"),
        ("file1.yaml", "file2.yaml", "plain", "result_plain.txt"),
        ("file1.json", "file2.json", "json", "result_json.txt"),
        ("file1.yaml", "file2.yaml", "json", "result_json.txt"),
    ],
)
def test_generate_diff(file1, file2, format, result):

    file1_path = os.path.join(TEST_DATA_DIR, file1)
    file2_path = os.path.join(TEST_DATA_DIR, file2)

    assert generate_diff(
        file1_path, file2_path, format) == read_fixture(result)