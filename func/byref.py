#参照渡し(byref) <-> 値渡し(byvalue)

# def add_nums(a, b):
#     print(f"aのアドレス：{id(a)}")
#     print(f"bのアドレス：{id(b)}")
#     return a + b
#
#
# one = 1
# two = 2
# print(f"oneのアドレス：{id(one)}")
# print(f"twoのアドレス：{id(two)}")
# print(add_nums(one, two))

# def add_one(num):
#     print(f"変更前のnumID：{id(num)}")
#     num += 1
#     print(f"変更後のnumID：{id(num)}")
#     return num
#
#
# one = 1
# print(f"oneのID：{id(one)}")
# num = add_one(one)
# print(f"関数呼び出し後のoneのID：{id(one)}")
# print(f"numのID：{id(num)}")

def add_fruit(fruits, fruit):
    print(f"変更前fruitsのID：{id(fruits)}")
    fruits.append(fruit)
    print(f"変更後fruitsのID：{id(fruits)}")
    return fruits


myfruits = ['apple', 'peacb', 'lemon']
myfruit = 'banana'
print(f"前fruits{myfruits}")
add_fruit(myfruits, myfruit)
print(f"後fruits{myfruits}")