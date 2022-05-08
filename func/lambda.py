# lambda関数(無名関数)

def square(x):
    return x * x

s = lambda x: x * x
print(square(3))
print(s(5))


def power(exponent):
    # def inner_power(base):
    #     return base ** exponent
    return lambda base: base ** exponent
    # return inner_power

third_power = power(3)
print(third_power(2))

numbers = [1, 5, 23, 54, 17, 48, 11, 8]
# filter()

# for num in numbers:
#     print(filterfunc(num))

filtered_num = filter(lambda num: num % 2, numbers)
print(list(filtered_num))