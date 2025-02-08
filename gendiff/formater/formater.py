from gendiff.formater.json import json_format
from gendiff.formater.plain import format_plain
from gendiff.formater.stylish import get_diff_format_stylish


def choice_formats(diff, formatter):
    if formatter == "stylish":
        return get_diff_format_stylish(diff)
    if formatter == "plain":
        return format_plain(diff)
