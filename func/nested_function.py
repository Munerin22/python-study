#関数の中で関数を定義（nested function）

msg = "I am global"
def outer(outer_param):
    msg = "I am outer"
    outer_param = "dog"
    def inner():
        nonlocal msg
        msg = "I am inner"
        inner_text = "inner_dog"
        print("This is inner function")
        print(outer_param)
        print(msg)
    inner()
    print(msg)


outer("outer arg")
print(msg)
# inner()
