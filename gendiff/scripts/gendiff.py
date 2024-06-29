import argparse
from gendiff import generate_diff
import json


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    args = parser.parse_args()
    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))
    rez = generate_diff(file1, file2)
    print(rez)


if __name__ == '__main__':
    main()
