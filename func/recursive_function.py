# 再帰関数(recursive function)：関数内で自身の関数をcallする関数
# 階乗 (factorical)：3! = 3 * 2 * 1 = 6
# n! = n * (n-1) * (n-2) ・・・・ * 1


def factrial(n):
    if n == 1:
        return 1
    else:
        return n * factrial(n-1)

# フィボナッチ数列：再帰関数ver
def fib(i):
    if i <= 1:
        return i
    else:
        return fib(i-1) + fib(i-2)

# フィボナッチ数列：再帰なしver
def fib_1(n):
    count = 0
    sub = []
    if n == 0:
        sub.append(0)
    else:
        for count in range(n+1):
            if len(sub) == 0:
                sub.append(0)
            elif int(sub[-1]) == 0:
                sub.append(1)
            else:
                sub.append(sub[-1] + sub[-2])
    return sub[-1]




print(fib_1(7))
# print(factrial(5))
# print(fib(5))
for i in range(50):
    print(i, fib_1(i))