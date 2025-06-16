import streamlit as st
import json
from Banking.account import SavingsAccount, CurrentAccount
from Banking.transaction import deposit, withdraw

# Function to save accounts to JSON
def save_accounts(data, filename="accounts.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Function to load accounts from JSON
def load_accounts(filename="accounts.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Load existing accounts
accounts = load_accounts()

# Home Page
st.title("🏦 UP Express Banking System")
st.subheader("LKO University Branch")

menu = st.sidebar.selectbox("Select Option", ["Create Account", "Login"])

if menu == "Create Account":
    st.header("Create Account")
    name = st.text_input("Enter your name")
    acc_type = st.selectbox("Choose account type", ["Savings", "Current"])
    initial_deposit = st.number_input("Enter initial deposit", min_value=0.0, step=0.01)

    if st.button("Create Account"):
        if acc_type.lower() == "savings":
            acc = SavingsAccount(name, initial_deposit)
        else:
            acc = CurrentAccount(name, initial_deposit)

        accounts[str(acc.account_number)] = {
            "name": acc.name,
            "balance": acc.get_balance(),
            "type": acc_type
        }
        
        save_accounts(accounts)  # Save to JSON file
        st.success(f"Account created successfully! Your account number is *{acc.account_number}*")

elif menu == "Login":
    st.header("Login to Your Account")
    acc_number = st.number_input("Enter your account number", min_value=1000, step=1)

    if st.button("Login"):
        accounts = load_accounts()  # Load latest accounts
        if str(acc_number) in accounts:
            user_acc_data = accounts[str(acc_number)]
            st.session_state["logged_in"] = True
            st.session_state["user_acc"] = user_acc_data
            st.session_state["acc_number"] = acc_number
        else:
            st.error("Account not found. Please check your account number.")

if "logged_in" in st.session_state and st.session_state["logged_in"]:
    user_acc_data = st.session_state["user_acc"]
    st.success(f"Welcome {user_acc_data['name']}!")
    
    action = st.radio("Choose an option", ["Deposit", "Withdraw", "Check Balance"])

    if action == "Deposit":
        amount = st.number_input("Enter amount to deposit", min_value=0.0, step=0.01)
        if st.button("Confirm Deposit"):
            user_acc_data["balance"] += amount
            accounts[str(st.session_state["acc_number"])] = user_acc_data
            save_accounts(accounts)
            st.success(f"Deposit of {amount} successful! New balance: {user_acc_data['balance']}")
            if st.button("Return to Menu"):
                del st.session_state["logged_in"]

    elif action == "Withdraw":
        amount = st.number_input("Enter amount to withdraw", min_value=0.0, step=0.01)
        if st.button("Confirm Withdrawal"):
            if user_acc_data["balance"] >= amount:
                user_acc_data["balance"] -= amount
                accounts[str(st.session_state["acc_number"])] = user_acc_data
                save_accounts(accounts)
                st.success(f"Withdrawal of {amount} successful! New balance: {user_acc_data['balance']}")
            else:
                st.error("Insufficient funds.")
            if st.button("Return to Menu"):
                del st.session_state["logged_in"]

    elif action == "Check Balance":
        st.info(f"Your current balance is: *{user_acc_data['balance']}*")
        if st.button("Return to Menu"):
            del st.session_state["logged_in"]