myvariable = "This is global variable"


def myfunc():
    print("This is my function!!")

# _(アンダースコア)を入れた関数はモジュール内でしか使用しない意思表示
def _anotherfunc():
    print("This is another function!!")

# moduleを開発する際にインポートによる不必要な実行を防ぐ
if __name__ == "__main__":
    print("This is mymodule")
    print(f"mymodule.__name__: {__name__}")