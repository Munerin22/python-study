# *argsと**kwargs

# *args:不特定多数
# print("hello", "world")
def get_average(*args):
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num
    print(*args)

average = get_average(1, 2, 3, 4, 5, 6)
print(average)

# **kwargs
def kwargs_func(**kwargs):
    # print(kwargs)
    param1 = kwargs.get('param1', 1)
    param2 = kwargs.get('param2', 2)
    param3 = kwargs.get('param3', 3)

    print(f"param1:{param1}, param2:{param2}, param3:{param3}")

kwargs_func(param1 = 10, param2 = 6, param3 = 25, param4 = 50)

# *と**はunpacking operator
numbers = (1, 2, 3)
print(*numbers)

a = {'a':1, 'b':2}
b = {'c':3, 'd':4}
c = {**a, **b}
print(c)