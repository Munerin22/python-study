import datetime

class Bank:
    account_number = 0

    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.id = account_number
        self.tran_log = ""
        print("新規に口座が作成されました")
        print(f"お名前:{self.name}, ID:{Bank.account_number}")
        Bank.account_number += 1


    def withdraw(self):
        print(f"{self.name}さんですね。")
        withdraw = input("引き落とし額を入力してください")
        if withdraw.isdecimal():
            withdraw = int(withdraw)
            print(f"引き落とし額は{withdraw}円です")
            if withdraw <= self.balance:
                balance = self.balance - withdraw
                print(f"{self.name}さんの口座ID:{self.id}残高は{balance}円です")
            else:
                print("残高が不足してます")
        else:
            print("整数値を入力してください")
        self.transaction("引き落とし", withdraw, balance)

    def deposit(self):
        print(f"{self.name}さんですね。")
        deposit = input("貯金額を入力してください")
        if deposit.isdecimal():
            deposit = int(deposit)
            balance = self.balance + deposit
            print(f"{self.name}さんの口座ID:{self.id}残高は{balance}円です")
        else:
            print("整数値を入力してください")
        self.transaction("貯金", deposit, balance)


    def transaction(self, tran, tran_money, balance):
        print("今回の取引結果")
        dt = str(Bank.date_log())
        print(dt)
        print(f"口座ID:{self.id}, 取引:{tran}, 取引額:{tran_money}, 残高:{balance}")

        self.tran_log = {"日時":dt, "口座ID":self.id, "取引":tran, "取引額":tran_money, "残高":balance}


    def tran_check(self):
        print(self.tran_log)

    @staticmethod
    def date_log():
        dt = datetime.datetime.now()
        return dt


mune = Bank("Mune", 12500, Bank.account_number)
Toki = Bank("Toki", 99999, Bank.account_number)

mune.withdraw()
mune.tran_check()