"""
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""


class bankWithdrawl:
    def __init__(self):
        self.D = 0
        self.W = 0

    def deposit(self, deposit):
        self.D += deposit

    def withdraw(self, withdraw):
        self.W = withdraw
        self.D -= withdraw

    def __str__(self):
        return f"Available: {self.D}"


obj = bankWithdrawl()
obj.deposit(300)
obj.deposit(300)
obj.withdraw(200)
obj.deposit(100)
print(obj)
