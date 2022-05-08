# 再帰関数(recursive function)：関数内で自身の関数をcallする関数
# 階乗 (factorical)：3! = 3 * 2 * 1 = 6
# n! = n * (n-1) * (n-2) ・・・・ * 1


def factrial(n):
    if n == 1:
        return 1
    else:
        return n * factrial(n-1)

def fib(i):

    return fib(i-1) + fib(i-2)


print(factrial(5))
print(fib(2))