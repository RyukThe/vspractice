def decorator(fun):
    def wrapper():
        print("About to print")
        fun()
        print("print the function")
    return wrapper
def sayHello():
    print("Hello")

some = decorator(sayHello)
some()






    