import pytest

from gendiff.generate_diff import generate_diff
from gendiff.reading_files import reading_files


@pytest.mark.parametrize(
    "file1, file2, result",
    [
        (
            "/User/rustemgb/python-project-50/tests/test_data/file1.json",
            "/User/rustemgb/python-project-50/tests/test_data/file2.json",
            "/User/rustemgb/python-project-50/tests/test_data/result_json.txt",
        )
    ],
)
def test_geberate_diff(file1, file2, result):
    assert generate_diff(file1, file2) == reading_files(result)
