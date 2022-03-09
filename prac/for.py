#forループ
# fruits = ['apple', 'banana', 'lemon', 'peach']
#
# for fruit in fruits:
#     print(f"I love {fruit}!!")
#
# for char in "Hello World":
#     print(f"char:{char}")

# iterationとiterable

# Challenge
fruits = ["リンゴ", "バナナ", "モモ", "レモン", "メロン", "パイナップル", "イチゴ"]
fruits_like = []
notlike = []

for fruit in fruits:
    like = input(f"{fruit}は好きですか？？はい/いいえ：")
    if like == "はい":
        fruits_like.append(fruit)
    elif like == "いいえ":
        notlike.append(fruit)

print(f"あなたの好きなフルーツは{list(fruits_like)}")
print(f"あなたの好きじゃないフルーツは{list(notlike)}")