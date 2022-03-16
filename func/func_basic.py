# 関数：コードの再利用
# print()
# len()
# input()

#華氏から摂氏に変換する
fahrenheit = 75
fahren = 55
# celsius = (fahrenheit - 32) * 5/9
# print(celsius)

# celsius = fahrenheit_to_celsius()

#関数 def（定義）
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
#ここまでが関数の定義


celsius = fahrenheit_to_celsius(fahren)
print(celsius)
