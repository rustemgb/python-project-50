import os

import pytest

from gendiff.generate_diff import generate_diff

DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")


def read_fixture(file_name):
    with open(os.path.join(DATA_DIR, file_name), "r") as file:
        return file.read().strip()


@pytest.mark.parametrize(
    "file1, file2, result",
    [
        (
            "file1.json", "file1.json", "result.txt"
        )
    ],
)
def test_generate_diff(file1, file2, result):

    file1_path = os.path.join(DATA_DIR, file1)
    file2_path = os.path.join(DATA_DIR, file2)

    expected = read_fixture(result)

    diff = generate_diff(file1_path, file2_path)
    assert diff == expected