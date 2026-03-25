# wrapping of data and function into single unit
# data hiding
class bank_account:
    def __init__(self, name, balance):
        self.name = name  # public
        self.__balance = balance  # protected
        # self._balance = balance  # protected

    def get__balance(self):  # getter function
        return self.__balance

    def set__balance(self, newbalance):
        self.__balance = newbalance


acc1 = bank_account("saphal", 1000)

acc2 = bank_account("rahul", 10000)
acc1.set__balance(30203)
print(acc1.name, acc1.get__balance())
