class BankAccount:
    def __init__(self,account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs {amount}")
            return
        print("Enter valid amount to deposite!")
        
    def withdraw(self,amount):
        if amount < 0:
            print("Enter valid ammount.")
            return
        
        if amount <= self.__balance:
            self.__balance -= amount
            print("Successfully withdrawn.")
            return
        print("Insufficient Amount.")
    
    def check_balance(self):
        print(f"Balance: {self.__balance}")
    
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print()

account1 = BankAccount("Alice",123456789, 25000)
account2 = BankAccount("Bob",987654321, 5000)

account1.display_account_info()
account2.display_account_info()

account1.deposit(5000)
account1.check_balance()
account1.withdraw(-500)
account1.check_balance()

account2.withdraw(5500)