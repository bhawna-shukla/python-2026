#create a account  class  with 2  attributes - balance and account no
#create  methods  for debit , credit & printing   the balance 

class Account:

    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debit ")
        print("total balance =" ,self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was creadit ")
        print("total balance =" ,self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000,234567)
print(acc1.account)
print(acc1.balance)
acc1.debit(1000)
acc1.credit(30000)
acc1.debit(10000)
acc1.credit(30000)
