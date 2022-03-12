# taple(タプル):変更できないリスト []ではなく()を使う

date_of_birth = (1990, 2, 3)
date_of_birth_list = [1990, 2, 3]
date_of_birth_list[0] = 2010
print(date_of_birth[0])
print(date_of_birth)

year, month, day = date_of_birth
print(year)
print(month)
print(day)