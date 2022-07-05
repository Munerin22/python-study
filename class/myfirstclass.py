class Person:

    # クラス変数
    num_legs = 2

    # インスタンスの生成->constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self): #メソッドは1行空けて書く. selfを入れること
        print(f"{self.name} is walking")

    def run(self):
        print(f"{self.name} is running")

john = Person("John", 28, 'male')
taro = Person("Taro", 18, 'male')
emma = Person("Emma", 40, 'female')


# インスタンス変数
# 「.」に続けてアクセス可能
print(john.name)
print(taro.age)

# インスタンス変数の更新
print(f"変更前:ジョンのageは{john.age}です")
john.age = 33
print(f"変更後:ジョンのageは{john.age}です")


# インスタンスメソッド
john.walk()
emma.walk()
taro.run()

print(f"ジョンの足は{john.num_legs}")
print(taro.num_legs)
Person.num_legs = 3
print(f"ジョンの足は{john.num_legs}")
john.num_legs = 5
print(f"ジョンの足は{john.num_legs}")
print(f"太郎の足は{taro.num_legs}")
