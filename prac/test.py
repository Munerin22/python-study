#python基礎認定用

# str = 'BeautifullsBetterThanUgly'
# print(str[100:120])

i = 6

def f(arg = i):
    i = 3
    print(arg)


i = 4
i = 2

f()

# def shop(name, *argsY, **argsX):
#     print("flowershop:", name)
#     keys = sorted(argsX.keys())
#     for kw in keys:
#         print(kw, ":", argsX[kw])
#     for Y in argsY:
#         print(Y)
#
#
# shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.",bouquet="Sunflower",plants="Pachira",dried="Rose")


# def scope():
#     loc = "init"
#     def do_local():
#         loc = "local"
#     def do_nonlocal():
#         # nonlocal loc
#         loc = "nonlocal"
#     def do_global():
#         nonlocal loc
#         loc = "nonlocal"
#         # global loc
#         # loc = "global"
#
#     do_local()
#     print("A:", loc)
#     do_nonlocal()
#     print("B:", loc)
#     do_global()
#     print("C:", loc)
#
# scope()
# loc = "aaa"
# print("D:", loc)

# import sys
# print(sys.argv[:])

