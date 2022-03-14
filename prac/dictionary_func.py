fruits_color = {'apple': 'red', 'lemon': 'yellow', 'peach': 'pink'}
# print(fruits_color['banana'])

if 'banana' in fruits_color:
    print(fruits_color['banana'])
else:
    print('the key is not found')

# .get()
fruit = input("フルーツの名前を指定してください")
print(fruits_color.get(fruit, 'Nothing'))

# .update()
fruits_color2 = {'banana': 'yellow', 'melon': 'green'}
fruits_color.update(fruits_color2)
print(fruits_color)