from decimal import Decimal, getcontext

getcontext().prec = 2  

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = Decimal(balance)

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += Decimal(amount)
        return "Deposited ${}. New balance: ${}".format(amount, self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if Decimal(amount) > self.balance:
            return "Insufficient funds."
        self.balance -= Decimal(amount)
        return "Withdrew ${}. New balance: ${}".format(amount, self.balance)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return "Account Number: {}, Account Holder: {}, Balance: ${}".format(
            self.account_number, self.account_holder, self.balance
        )

    def __repr__(self):
        return "BankAccount('{}', '{}', {})".format(
            self.account_number, self.account_holder, self.balance
        )


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = Decimal(interest_rate)

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        return self.deposit(interest)

    def __str__(self):
        return "{}, Interest Rate: {}".format(
            super().__str__(), self.interest_rate
        )

    def __repr__(self):
        return "SavingsAccount('{}', '{}', {}, {})".format(
            self.account_number, self.account_holder, self.interest_rate, self.balance
        )


bank_account = BankAccount("20000", "Hamzah account")
print(bank_account.deposit(1000))
print(bank_account.withdraw(500))
print(bank_account)

savings_account = SavingsAccount("4800", "user account", interest_rate=0.05)
print(savings_account.apply_interest())
print(savings_account)
