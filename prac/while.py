# whileループ
# count = 0
# while count < 10:
#     print(count)
#     count += 1
#
# #break と continue
# while True:
#     age = int(input("あなたは何歳ですか？"))
#     if not 0 <= age < 120:
#         print("入力された値は正しくありません")
#     else:
#         print(f"あなたは{age}歳ですね")
#         break

#Challenge
age = int(input("おいくつですか？"))

if age >= 18:
    print(f"{age}歳なのでカジノに入れます")

    while True:
        print("今遊べるゲームは、1：ルーレット、2：ブラックジャック、3：ポーカー")
        game = int(input("遊びたいゲームの番号を教えてください"))
        if not (game == 1 or game == 2 or game == 3):
            continue
        elif game == 1:
            print(f"{game}番のルーレットで遊びます")
            break
        elif game == 2:
            print(f"{game}番のブラックジャックで遊びます")
            break
        elif game == 3:
            print(f"{game}番のポーカーで遊びます")
            break
else:
    print(f"{age}歳なのでカジノに入れないです")