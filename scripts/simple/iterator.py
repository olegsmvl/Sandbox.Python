if __name__ == "__main__":
    a = [1, 2, 3]
    it = iter(a)
    print(next(it))
    print(next(it))
    print(next(it))
    b = "some"
    it = iter(b)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print("===========")
    print(b[-2])
