#input(): ユーザーの入力した値（文字列）を取得する

#age = input("何歳ですか")
#ageには文字列で入力される
#print(f"あなたは{age}歳です")

#Challenge
age = input("おいくつですか？")

if int(age) >= 18:
    print(f"{age}歳なのでカジノに入れます")

    print("今遊べるゲームは、1：ルーレット、2：ブラックジャック、3：ポーカー")
    game = input("遊びたいゲームの番号を教えてください")
    if int(game) == 1:
        print(f"{game}番のルーレットで遊びます")
    elif int(game) == 2:
        print(f"{game}番のブラックジャックで遊びます")
    elif int(game) == 3:
        print(f"{game}番のポーカーで遊びます")
    else:
        print("遊べるゲームがありません")
else:
    print(f"{age}歳なのでカジノに入れないです")