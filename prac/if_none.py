#if文のNoneの取り扱い
a = None
if a is None:
    print("a is None!!")
else:
    print("a has value!")

if not a:
    print("a is None")
    a = 10
    print(f"a is {a}")