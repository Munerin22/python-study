# 変数の代入：assignment

hello = "1. Hello"
world = "World"

print(hello+world)
print("2. format {}".format("world"))

name = "Mune"

print("3. Hey {} How are you doing?".format(name))

#fstring
# print(f"{hello} {world}")
# print(f"3. Hey {name} How are you doing?")

#built in function
#type()
hello_type = type(1.3)
print(hello_type)

#id()
hello_id = id("hello")
print(hello_id)