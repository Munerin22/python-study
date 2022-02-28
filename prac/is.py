#is 演算子：同じオブジェクトがどうかを判定する
#同じデータかどうかを判断
a = 1
b = 1
c = 3
d = a
e = c - (a+b)
print(a is b)
print(f"a is {id(a)}")
print(f"b is {id(b)}")
print(a is not c)
print(f"a is d = {a is d}")
print(f"a is e = {a is e}")

hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o"
print(hello, hello2)
print(hello is hello2)
hello = "morning"
print(hello is hello2)

#Noneかどうかの判定
nothing = None
print(nothing is None)

