#%%
class Teacher: #class - template for creating objects
#how do we define attributes?
#we define a special method called constructor 
    def __init__(self, name, age, salary): #constructor
        self.name = name
        self.age = age
        self.salary = salary

    def getSalary(self):
        print(self.salary)

alex = Teacher("Alex", 42, 2000)
Jhon = Teacher("Jhon", 27, 4000)
alex.getSalary() #to call method always use parentheses at end

# %%
class BankAccount:
    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance
    
    def displayCurrentBalance(self):
        print("Account Holder: ", self.accountHolder)
        print("Current Balance: ", self.balance)


account_1 = BankAccount("Elon Musk", 300000000)
account_2 = BankAccount("Sophie Schaesberg", 10)
account_1.displayCurrentBalance()

# %%
# add name input
class BankAccount:
    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance
    
    def displayCurrentBalance(self):
        print("Account Holder: ", self.accountHolder)
        print("Current Balance: ", self.balance)

#account_1 = BankAccount("Elon Musk", 300000000)
#account_2 = BankAccount("Sophie Schaesberg", 10)
#account_1.displayCurrentBalance()

accountHolder = input ("What is your name?")
balance = input ("How much money do you currently have?")

anonymous = BankAccount(accountHolder, balance)

anonymous.displayCurrentBalance()

# %%
# Exercise 3
class BankAccount:
    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance
    
    def displayCurrentBalance(self):
        print("Account Holder: ", self.accountHolder)
        print("Current Balance: ", self.balance)
    
    def deposit(self, add): #BE CAREFUL - you're calling the method "deposit", not the add
        self.balance += add

    def withdraw(self, subtract):
        self.withdraw -= subtract

account_1 = BankAccount("Elon Musk", 300000000)
account_2 = BankAccount("Sophie Schaesberg", 10)

account_2.deposit(100)
account_2.displayCurrentBalance()

# %%
# Exercise 4
class BankAccount:
    def __init__(self, accountHolder, balance): #, transactions = []):
        self.accountHolder = accountHolder
        self.balance = balance
        self.transactions = []
    
    def displayCurrentBalance(self):
        print("Account Holder: ", self.accountHolder)
        print("Current Balance: ", self.balance)
    
    def deposit(self, add):
        self.balance += add
        self.transactions.append("You have deposited: " + str(add))

    def withdraw(self, subtract):
        self.balance -= subtract
        self.transactions.append("You have withdrawn: " + str(subtract))

account_1 = BankAccount("Elon Musk", 300000000)
account_2 = BankAccount("Sophie Schaesberg", 10)

account_2.deposit(100)
account_2.withdraw(20)
account_2.displayCurrentBalance()
account_2.transactions

