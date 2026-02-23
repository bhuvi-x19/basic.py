class BankAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.__pin = pin
        self.__balance = balance

    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        print(f"Current Balance: {self.__balance}")


# Create account
name = input("Enter your name: ")
pin = input("Set a 4-digit PIN: ")

account = BankAccount(name, pin)

while True:     # infinite loop to keep the program running until the user exits.
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        entered_pin = input("Enter PIN: ")
        if account.verify_pin(entered_pin):
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        else:                                                                                                                                                  
            print("Incorrect PIN")

    elif choice == "2":
        entered_pin = input("Enter PIN: ")
        if account.verify_pin(entered_pin):
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("Incorrect PIN")

    elif choice == "3":
        entered_pin = input("Enter PIN: ")
        if account.verify_pin(entered_pin):
            account.check_balance()
        else:
            print("Incorrect PIN")

    elif choice == "4":
        print("Thank you for using the bank system!")
        exit()

    else:
        print("Invalid choice. Try again.")
        exit()

print(len("Hello"))
print(len([1, 2, 3, 4, 5]))
print(5+3)
print("5"+"3")
def a,b:
    return a+b
print(add(2,3))

print(add("Hello","World"))

class animal:
    def sound(self):
        print("The animal makes a sound")
        
class dog(animal):
    def sound(self):
        print("The dog barks")
        
class cat(animal):
    def sound(self):
        print("The cat meows")
        
d=dog()
d.sound()

c=cat()
c.sound()

abstraction
             