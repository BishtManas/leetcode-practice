class Bank:

    def __init__(self, balance: list):
        self.balance = balance

    def isValid(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.isValid(account1) or not self.isValid(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False

        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.isValid(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.isValid(account):
            return False
        if self.balance[account - 1] < money:
            return False

        self.balance[account - 1] -= money
        return True


if __name__ == "__main__":
    bank = Bank([10, 100, 20, 50, 30])

    print(bank.withdraw(3, 10))   # True
    print(bank.transfer(5, 1, 20)) # True
    print(bank.deposit(5, 20))     # True
    print(bank.transfer(3, 4, 15)) # False
    print(bank.withdraw(10, 50))   # False