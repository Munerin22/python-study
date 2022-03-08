#in 演算子
#fruits = ['apple', 'peach', 'banana']
#print('lemon' not in fruits)
#print('h' not in 'world')

#Challenge
fruit = input("好きなフルーツは何ですか？（カタカナで入力してね！）")

fruits = ["リンゴ", "モモ", "バナナ"]
print(f"果物の種類：{fruits}")
if fruit in fruits:
    fruits.remove(fruit)
else:
    fruits.append(fruit)

print(f"果物の種類更新：{fruits}")