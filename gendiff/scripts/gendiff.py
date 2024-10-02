import argparse
from gendiff import parsing
from gendiff import diff_build
from gendiff import format_data


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    args = parser.parse_args()
    dic1 = parsing(args.first_file)
    dic2 = parsing(args.second_file)
    diff = diff_build(dic1, dic2)
    rez = format_data(diff)
    print(rez)


if __name__ == '__main__':
    main()
