class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn. New balance: ${self.balance:.2f}")

    def run(self):
        while True:
            print("\n=== ATM Menu ===")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter deposit amount: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter withdrawal amount: "))
                self.withdraw(amount)
            elif choice == '4':
                print("Exiting the system. Thank you for using the ATM!")
                break
            else:
                print("Invalid option. Please try again.")

def main():
    # Initial balance can be set here
    initial_balance = 1000.0
    atm = ATM(initial_balance)
    atm.run()

if __name__ == "__main__":
    main()
