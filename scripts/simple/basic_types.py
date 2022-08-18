def main():
    a = { 1: "ff", 2: "mm"}
    print(type(a))

def main2():
    a = [ 1, 2, 3]
    print(type(a))
    print(id(a))
    b = a.copy()
    print(id(b))

def get_message(num: int)->str:
    return 10 * num

if __name__ == "__main__":
    #main()
    #x = get_message(5);
    #print(x)
    #print(type(x))
    main2()