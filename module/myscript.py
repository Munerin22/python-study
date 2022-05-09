# モジュールの全てをインポート
# import mymodule

# import mymodule as mm
# as を付けることでmm.myfuncのように呼べる

# 特定の関数のみインポート:myfuncのみ
from mymodule import myfunc, myvariable

# fromの場合、mymoduleはインポートしていないことになる
# mymodule.myfunc()
myfunc()


# print(mymodule.myvariable)
print(myvariable)

