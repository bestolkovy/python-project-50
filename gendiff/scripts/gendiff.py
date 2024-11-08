from gendiff import arg_pars
from gendiff import generate_diff


def main():
    dict1, dict2, format = arg_pars()
    result = generate_diff(dict1, dict2, format)
    print(result)


if __name__ == '__main__':
    main()
