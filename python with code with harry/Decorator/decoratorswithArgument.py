def repeate(n):
    def decorator(fun):
        def wrapper(a):
            for i in range(n):
                fun(a)
        return wrapper
    return decorator

@repeate(7)
def say_hello(a):
    print(f"Hello, {a}")

say_hello("Saurav")

'''
def decorator(fun):
    def wrapper(a):
        for i in range(n):
            say_hello(a)
    return wrapper
'''