#数値型
#int:整数→1, 2, 3
print(type(-100))

#float:浮動小数点
print(type(0.1))
print(0.1 + 0.1 + 0.1)

#Numeric Operator:数値演算子
#四則演算
print(1 + 0.4)
print(1 - 0.4)
print(2 * 3)
print(1 / 2)
print(5*6 + 3/6)
result = 1 + 0.1
print(f"type of result :{result} is {type(result)}")

#その他の演算
#floor division
print(14 // 3)
#modulo 剰余（余り）
print(14 % 3)
#指数
print(4 ** 3)

hit_point = 100
attack_point = 40.3
remain = hit_point - attack_point
print(f"remain hit point is {remain}")

#augmented assignment
a = 1
#a = a + 1
print(f"aの値は{a}")
a += 1 #34行目と同じ
print(f"a += 1 すると{a}")