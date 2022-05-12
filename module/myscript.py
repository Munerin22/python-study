import sys
# 標準ライブラリ、サードパーティーのライブラリ、自分たちのライブラリ、ローカルのライブラリ
# モジュールの全てをインポート
# import mymodule
sys.path.append("/Users/sg7sc/desktop/python-study/func")
import docstring
# 最初にビルトインモジュールを探しに行く
# 無ければsys.pathを見に行く→モジュールを探しに行く


# import mymodule as mm
# as を付けることでmm.myfuncのように呼べる

# 特定の関数のみインポート:myfuncのみ
from mymodule import myfunc, myvariable

# fromの場合、mymoduleはインポートしていないことになる
# mymodule.myfunc()
# myfunc()
# print(mymodule.myvariable)
# print(myvariable)

print(sys.path)
print(docstring.multiply(3, 4))