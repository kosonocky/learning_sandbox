

def test():
    x = 2
    y = 2
    print(id(x))
    print(id(y))
    

def main():
    print(locals())
    test()
    print(locals())
    x = 2
    print(id(x))
    print(locals())
if __name__ == '__main__':
    main()