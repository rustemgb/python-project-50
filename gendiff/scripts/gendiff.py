from gendiff.cli import cli_parser
from gendiff.generate_diff import generate_diff


def main():
    first_file, second_file = cli_parser()
    diff = generate_diff(first_file, second_file)
    print(diff)


if __name__ == "__main__":
    main()