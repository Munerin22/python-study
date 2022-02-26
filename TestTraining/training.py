#name1,name2,name3,name4 = '', 'suzuki', 'tanaka', 'sato'
#selected_name = name1 or name2 or name3 or name4
#print(selected_name)

#from math import pi
#str_pi = [str(round(pi, i)) for i in range(0, 5)]
#print(str_pi)

#num_list = [2, 4, 6, 4, 4, 2, 6]
#for i in range(num_list.count(6)):
#   print(i, end='')

#titles = {'title1': 'hoge1', 'title2': 'hoge2', 'title3': 'hoge3'}

#print("出力結果:")
#for k, v in titles.items():
#   print(v)

#x = ["a","b","c","d","e"]
#print(x[:-1])

#dive_into_code = [(9, 'Poro'), (2, 'Nakao'), (5, 'Miyaoka'), (4, 'Kimura')]
#dic = dive_into_code
#dic.sort(key=lambda dic:dic[0])

#print(dic[:])

#d = 'dive\ninto\ncode\t'

#print(len(d))

def fugafuga(title, content='default_content', number=4):
    content = 'content'
    title = 'try!'

    print(title, end=' ')
    print(content, end=' ')
    print(number)

fugafuga(title='title_default', content='None', number=1)

print("出力結果:",end='')
try:
  #raise IOError("開始前","Exception発生")
  print("開始")
except IOError as msg:
  print("IOError発生:",msg.args[0])
except Exception as msg:
  print("予期せぬ問題発生:",msg.args[1])
else:
  print("Else表示")