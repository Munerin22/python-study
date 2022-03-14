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
game_text = "プレイするゲームを選択してください" \
            "1:ルーレット" \
            "2:ブラックジャック" \
            "3:ポーカー"
game_dict = {1: 'ルーレット', 2: 'ブラックジャック', 3: 'ポーカー'}
# print(game_dict.keys())

if age >= 18:
    print(f"{age}歳なのでカジノに入れます")

    while True:
        print("遊びたいゲームの番号を教えてください")
        for number, play in game_dict.items():
            print(f"{number}:{play}")
        game = int(input(":"))

        if game_dict.get(game, None):
            print(f"{game}番の{game_dict[game]}で遊びます")
            break
else:
    print(f"{age}歳なのでカジノに入れないです")