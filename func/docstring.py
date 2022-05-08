# docstring:関数の説明を作れる
# 組織の書き方に合わせる

def multiply(num1, num2):
    """
    multiply num1 with num2 and return the rerult
    :rtype: object
    :param num1:
    :param num2:
    :return: num1 * num2
    """

    return num1 * num2


# multiply()

print(multiply.__doc__)
