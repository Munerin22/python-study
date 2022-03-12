#dictionary:キーと値の組み合わせを複数保持するデータ型
fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'peach': 'pink'}
# print(fruits_colors['peach'])
# fruits_colors['melon'] = 'green'
# print(fruits_colors)
# fruits_colors['apple'] = 'iphone'
# print(fruits_colors)

dict_sample = {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four': {'inner': 'dict'}}
# print(dict_sample['four']['inner'])

colors = {}
colors[1] = 'blue'
colors[0] = 'red'
colors[3] = 'green'
# print(colors)

#for文で使うとき
# .keys() .values()
for x in fruits_colors:
    print(x)

# .items()
for fruit, color in fruits_colors.items():
    print(f"{fruit} is {color}")