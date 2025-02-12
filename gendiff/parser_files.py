import json
import os

import yaml


def reading_files(file_path):
    with open(file_path) as file:
        return file.read()


def get_format_file(file_path):
    _, format_file = os.path.splitext(file_path)
    return format_file[1:]


def parser_data(data, format):
    if format == "json":
        return json.loads(data)
    if format == "yaml" or format == "yml":
        return yaml.load(data, Loader=yaml.SafeLoader)


def parser_data_from_file(file_path):
    format_file = get_format_file(file_path)
    file_data = reading_files(file_path)
    return parser_data(file_data, format_file)
