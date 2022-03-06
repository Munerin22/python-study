#リスト（lists）：複数のオブジェクトを順序づけて保存するデータ型
# []で括って、,(カンマ)で各オブジェクトを区切る

fruits = ['apple', 'peach', 'greapes', 'melon']
hetro_list = ['string', 1, 3.4, True, fruits]
#オブジェクト
#'1'
#1
#1.0
#True
#False

#print(hetro_list[-1][-2])
#print(fruits[-1])

#.append: 新しいオブジェクトを追加する
#.insert: 指定したindexに指定したオブジェクトを追加する
#.remove: マッチした最初のオブジェクトを除く
#.sort: 昇順に並び替える
# len(): リストの要素数を取得する
print(fruits)
fruits.append('banana')
print(fruits)
fruits.insert(3, 'lemon')
print(fruits)
fruits.remove('peach')
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

print(len(fruits))