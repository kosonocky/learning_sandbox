
class Parent():
    def __init__(self):
        self._a = 1
        self._b = 2

    def add_one_to_self(self):
        self._a += 1
        self._b += 1


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.__c = 3

    def show(self):
        print(self._a)
        print(self._b)
        print(self.__c)


def main():
    child = Child()
    child.add_one_to_self()
    child.show()


if __name__ == '__main__':
    main()
