from Banking.account import SavingsAccount, CurrentAccount
from Banking.transaction import deposit, withdraw

accounts={}
def create_account():
    name = input("Enter your name: ").strip()
    acc_type = input("Enter account type (Savings/Current): ").strip().lower()
    initial_deposit = float(input("Enter initial deposit: "))
    if acc_type == "savings":
        acc = SavingsAccount(name, initial_deposit)
    elif acc_type == "current":
        acc = CurrentAccount(name, initial_deposit)
    else:
        print("Invalid account type. Please choose Savings or Current.")
        
    accounts[acc.account_counter] = acc
    print(f"\n----Account created successfully. Your account number is {acc.account_counter}----")

def login():
    acc_number = int(input("Enter your account number: "))
    if acc_number in accounts:
        user_acc = accounts[acc_number]
        print(f"\nWelcome {user_acc.name}!")
        while True:
            print("\n1. Deposit")
            print("\n2. Withdraw")
            print("\n3. Check Balance")
            if isinstance(user_acc, SavingsAccount):
                print("\n4. Calculate Interest")
            print("\n5. Logout")

            choice = input("Choose an option: ")
            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                deposit(user_acc, amount)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                withdraw(user_acc, amount)
            elif choice == "3":
                print(f"Your current balance is: {user_acc.get_balance()}")
            elif choice == "4" and isinstance(user_acc, SavingsAccount):
                user_acc.calculate_interest()
            elif choice == "5":
                print("Logging out...")
                break
    else:
        print("Account not found. Please check your account number.")

def main():
    print("\nWelcome to the American Express Banking System".center(50))
    print('Nagpur University Branch'.center(50))

    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\n******Thank you for using the American Express Banking System. Goodbye!******")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()