#論理演算子(logical operator)
#and, or, not
a = 1
b = 1
c = 10
d = 100
print(a == b and c > d)
print(a == b or c > d)
print(not a == b)

old = 10
hight = 109
print(f"あなたは{old}歳で{hight}cmなので{old >= 10 and hight >= 110}です")
master = True
experience = 4
print(f"あなたは修士号：{master}、実務経験{experience}年なのでVisaの取得は{master or experience >= 5}です")
