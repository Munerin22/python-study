fruits = ['apple', 'peach', 'lemon', 'banana']
#for else
# for fruit in fruits:
#     choice = input(f"あなたが探しているフルーツは{fruit}ですか？はい/いいえ")
#     if choice == "はい":
#         print("見つかりました")
#         break
#     else:
#         print("違いますか…")
# else:
#     print("ループが回り切った！！")

# #while else
# count = 0
# while count < 10:
#     print(count)
#     count += 1
# else:
#     print("countは10以上になりました")

balance = 800
game_price = 200

while balance >= game_price:
    choice = input(f"1回200円のゲームをしますか？(残高は{balance}円)y/n")
    if choice == "y":
        balance -= game_price
        print(f"残高は{balance}円")
        if balance < game_price:
            print("残高が足りないのでゲームができないです")
            break
    elif choice == "n":
        print("また遊びましょう")
        #break
    else:
        print("yかnで答えてください")