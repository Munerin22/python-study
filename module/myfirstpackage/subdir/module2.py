from .module3 import myfunc3

def myfunc():
    print("This is myfunc from module 2")


def myfunc2():
    print("This is myfunc2 from module 2")
    myfunc3()
