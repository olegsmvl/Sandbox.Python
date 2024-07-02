def logger(func):
    def wrapper(name):
        print("Something is happening before the function is called.")
        func(name)
        print(f"logged: {name}")
        print("Something is happening after the function is called.")
    return wrapper

@logger
def say_hello(name):
    print(f"Hello {name}!")

say_hello("alice")