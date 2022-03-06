#if分

age = 19
age_alcohol = 21
if age >= age_alcohol:
    print("You can drink beer!")
else:
    print("You are too young to drink beer")

age_drive = 18
if age >= age_alcohol:
    print("You can drink beer!")
elif age < age_drive:
    print("You cannot even drive")
else:
    print("You are not allowed to drink beer but you can drive only if you have a license")

if not 0 < age < 120:
    print("The value is invalid")

#Challenge
balance = 100000
withdraw = 80000
if balance > withdraw:
    if 0 < withdraw <= 1000000:
        print("引き出しを実行します")
        balance = balance - withdraw
        print(f"残高を更新します。残高は{balance}円です")
    elif 1000000 < withdraw:
        print("引き出し額の上限を超えています")
    else:
        print("金額入力エラー")
else:
    print("引き出しができません")

