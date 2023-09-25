class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.amount = amount
        if int(amount) > int(self.balance):
            return self.balance
        else:
            self.balance = int(self.balance) - int(amount)
            return self.balance
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = int(amount) + int(self.balance)
        return self.balance
            

    def __str__(self):
        return "%s(%s원)" %(self.name, self.balance)
    

c1 = Customer('Bill')
c2 = Customer('Steve', 50000)
c3 = Customer('TIm', 100000)
print(c1,c2,c3)

c1.deposit(50000)
c2.deposit(30000)
c3.withdraw(100000)
print(c1, c2, c3)

c2.withdraw( 1000000 )
print(c1, c2, c3)
print( c3.withdraw(10000), c2.deposit(10000) )
print(c1, c2, c3)

