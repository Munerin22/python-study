def print_name_local():
    first_name = "Taro"
    last_name = "Yamada"
    print(f"I'm {first_name} {last_name}")


print_name_local()

#グローバル変数（モジュール変数）
age = 30

def print_age():
    global age
    age = 20    #ローカル変数
    print(f"I'm {age} years old")
    # ローカルで変数を探して、無ければグローバル変数を参照する


print_age()
print(age)