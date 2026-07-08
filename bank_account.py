class BankAccount:
    def __init__(self,account_number,account_holder,balance) :
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    
    def deposit(self,money):
        self.balance+=money
    
    def withdraw(self,money):
        if money<=self.balance:
            self.balance-=money
        else:
            print("insufficient balance")
    def display(self):
        print("account balance",self.balance)
        
class SavingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance,interest_rate):
        self.interest_rate=interest_rate
        super().__init__(account_number, account_holder, balance)
    
    def add_interest(self):
        interest=self.balance*self.interest_rate/100
        self.balance+=interest
        print("Interest added",interest)
        
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance,overdraft_limit):
        self.overdraft_limit=overdraft_limit
        super().__init__(account_number, account_holder, balance)
        
    def withdraw(self,money):
        if money<=self.balance+self.overdraft_limit:
            self.balance-=money
        else:
            print("Overdraft limit exceeded")
    

print("Account Type")
print("1. Saving")
print("2. Current")

choice = int(input("Enter choice: "))

acc_no = int(input("Enter Account Number: "))
acc_holder = input("Enter Holder Name: ")
bal = float(input("Enter Balance: "))

if choice == 1:
    interest = int(input("Enter Interest Rate: "))
    account = SavingAccount(acc_no, acc_holder, bal, interest)

elif choice == 2:
    limit = float(input("Enter Overdraft Limit: "))
    account = CurrentAccount(acc_no, acc_holder, bal, limit)

else:
    print("Invalid Choice")
    exit() 
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Add Interest (Savings Only)")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        money = float(input("Enter amount: "))
        account.deposit(money)

    elif ch == 2:
        money = float(input("Enter amount: "))
        account.withdraw(money)

    elif ch == 3:
        account.display()

    elif ch == 4:
        if isinstance(account, SavingAccount):
            account.add_interest()
        else:
            print("Interest is available only for Savings Account.")

    elif ch == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")