#Program 13: Encapsulated Banking System with Inheritance Models

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"Deposited: Rs. {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: Rs. {amount:.2f}")

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Holder:", self.account_holder)
        print(f"Balance: Rs. {self.__balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0,
                 interest_rate=0.04):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: Rs. {interest:.2f}")

    def display(self):
        print("\nSavings Account")
        super().display()
        print(f"Interest Rate: {self.interest_rate * 100:.2f}%")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0,
                 overdraft_limit=5000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.get_balance() + self.overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            # Use the parent withdrawal method when
            # the account has sufficient balance.
            if amount <= self.get_balance():
                super().withdraw(amount)
            else:
                shortfall = amount - self.get_balance()
                super().withdraw(self.get_balance())
                print(f"Overdraft used: Rs. {shortfall:.2f}")
                print("Note: Overdraft usage is not stored separately.")
                
    def display(self):
        print("\nCurrent Account")
        super().display()
        print(f"Overdraft Limit: Rs. {self.overdraft_limit:.2f}")


# Main program
savings = SavingsAccount("Aman", 10000)
current = CurrentAccount("Rahul", 5000)

savings.display()
savings.deposit(2000)
savings.withdraw(1500)
savings.add_interest()
savings.display()

current.display()
current.deposit(1000)
current.withdraw(2000)
current.display()