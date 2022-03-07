#「:」を使って、複数の要素をとってくることができる(slicing)
even = [2, 4, 6, 8, 10, 12]
#基本は[開始：未満]
print(even[1:4])
print(even[:4])
print(even[3:-1])
print(even[3:])
print(even[:])

text = "hello world"
print(text[::-1])