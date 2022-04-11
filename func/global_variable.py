# call_count = 0

CALL_COUNT = 0 # constant variable
#python開発者から見て弄っていけない変数だと認識される

#なるべくローカルで変数を扱う。関数からグローバルを変更しないように→バグの元になる
def print_count1():
    global CALL_COUNT
    CALL_COUNT += 1
    print(f"関数1：{CALL_COUNT}回目")


def print_count2():
    global CALL_COUNT
    CALL_COUNT += 1
    print(f"関数2：{CALL_COUNT}回目")


print_count1()
print_count2()
print_count1()
print_count2()
