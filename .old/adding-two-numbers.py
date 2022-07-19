def add_1(a, b):
    return a+b


class algebra():
    # @staticmethod
    def add_2(a, b):
        return a+b


def main():
    print(f'method 1: {add_1(2,5)}')
    print(f'method 2: {algebra.add_2(2,5)}')


if __name__ == '__main__':
    main()
