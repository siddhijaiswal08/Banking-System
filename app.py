# enhanced_bank_app.py
import streamlit as st
import json
import hashlib
from datetime import datetime
import pandas as pd
import random

# ---------------------- Account Classes ---------------------- #
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = random.randint(1000, 9999)

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def apply_interest(self, rate=0.04):
        self.balance += self.balance * rate / 12

class CurrentAccount(BankAccount):
    pass

# ---------------------- Utility Functions ---------------------- #
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_accounts(data, filename="accounts.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_accounts(filename="accounts.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

accounts = load_accounts()

# ---------------------- Streamlit App ---------------------- #
st.set_page_config(page_title="UP Express Banking", layout="centered", page_icon="🏦")

# CSS Styling
st.markdown("""
    <style>
    .main {background-color: #fafafa;}
    .stButton>button {width: 100%; border-radius: 8px;}
    .stSelectbox>div>div {border-radius: 8px;}
    </style>
""", unsafe_allow_html=True)

# Init state
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------------- Home Page ---------------------- #
if st.session_state.page == "home":
    st.markdown("""
        <style>
        .title-section {
            margin-top: 40px;
            margin-bottom: 20px;
            text-align: center;
        }
        .subtitle {
            font-size: 22px;
            color: #333;
            margin-top: 10px;
            margin-bottom: 80px;
        }
        .section-title {
            font-size: 28px;
            font-weight: 600;
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .card {
            background-color: white;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 0 15px rgba(0,0,0,0.05);
            margin-bottom: 10px;
            height: 180px;
        }
        .card h3 {
            margin-top: 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and tagline
    st.markdown("""
        <div class="title-section">
            <h1>🏦 UP Express Banking System</h1>
            <div class="subtitle">🔐 Trusted. Safe. Modern Banking</div>
        </div>
    """, unsafe_allow_html=True)

    # Why Choose Section
    st.markdown("<div class='section-title'>Why choose UP Bank🚩?</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="card" style="background-color:#f5f8ff;">
                <h3>🔐 Secure</h3>
                <p>Your data is protected with top-tier encryption.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card" style="background-color:#f5fff5;">
                <h3>📜 Compliant</h3>
                <p>Fully regulated under university financial law.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="card" style="background-color:#fff5fa;">
                <h3>🧑‍🎓 Student-first</h3>
                <p>Designed for easy banking for students.</p>
            </div>
        """, unsafe_allow_html=True)

    # Get Started section
    st.markdown("<br><hr><br>", unsafe_allow_html=True)
    st.markdown("### 🚀 Get Started Today")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔑 Login"):
            st.session_state.page = "login"
    with col2:
        if st.button("🧾 Register"):
            st.session_state.page = "register"


# ---------------------- REGISTER PAGE ---------------------- #
elif st.session_state.page == "register":
    st.header("🧾 Open a New Bank Account")
    with st.form("register_form"):
        name = st.text_input("👤 Full Name")
        acc_type = st.selectbox("🏦 Account Type", ["Savings", "Current"])
        initial_deposit = st.number_input("💵 Initial Deposit", min_value=0.0, step=0.01)
        password = st.text_input("🔑 Set Password", type="password")
        submitted = st.form_submit_button("✅ Register")

        if submitted:
            acc = SavingsAccount(name, initial_deposit) if acc_type.lower() == "savings" else CurrentAccount(name, initial_deposit)
            accounts[str(acc.account_number)] = {
                "name": acc.name,
                "balance": acc.get_balance(),
                "type": acc_type,
                "password": hash_password(password),
                "transactions": []
            }
            save_accounts(accounts)
            st.success(f"🎉 Account created! Your account number is **{acc.account_number}**")
            st.session_state.page = "home"
            st.rerun()

# ---------------------- LOGIN PAGE ---------------------- #
elif st.session_state.page == "login":
    st.header("🔐 User Login")
    with st.form("login_form"):
        acc_number = st.number_input("🆔 Account Number", min_value=1000, step=1)
        password_input = st.text_input("🔑 Password", type="password")
        login_submit = st.form_submit_button("🚪 Login")

        if login_submit:
            accounts = load_accounts()
            if str(acc_number) in accounts:
                user_acc_data = accounts[str(acc_number)]
                if hash_password(password_input) == user_acc_data["password"]:
                    st.session_state.logged_in = True
                    st.session_state.user_acc = user_acc_data
                    st.session_state.acc_number = acc_number
                    st.session_state.page = "dashboard"
                    st.rerun()
                else:
                    st.error("❌ Incorrect password.")
            else:
                st.error("❌ Account not found.")

# ---------------------- DASHBOARD ---------------------- #
elif st.session_state.page == "dashboard":
    user_acc_data = st.session_state["user_acc"]
    acc_number = st.session_state["acc_number"]

    st.markdown(f"""
        <div style='background-color:#f0f2f6; padding:15px; border-radius:10px; margin-bottom:10px;'>
            <h4>👋 Welcome, {user_acc_data['name']}!</h4>
            <p><b>Account No:</b> {acc_number} &nbsp; | &nbsp; <b>Type:</b> {user_acc_data['type']}</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.metric(label="💰 Current Balance", value=f"₹ {user_acc_data['balance']:.2f}")
    with col2:
        if st.button("🚪 Logout"):
            for key in ["logged_in", "user_acc", "acc_number"]:
                del st.session_state[key]
            st.session_state.page = "home"
            st.success("👋 Logged out successfully!")
            st.rerun()

    st.markdown("---")
    action = st.radio("⚙️ Banking Operations", ["Deposit", "Withdraw", "Check Balance", "Transaction History"], horizontal=True)

    if action == "Deposit":
        amount = st.number_input("💵 Enter deposit amount", min_value=0.0, step=0.01, key="deposit")
        if st.button("💳 Confirm Deposit"):
            user_acc_data["balance"] += amount
            user_acc_data["transactions"].append({
                "type": "deposit",
                "amount": amount,
                "balance": user_acc_data["balance"],
                "timestamp": str(datetime.now())
            })
            accounts[str(acc_number)] = user_acc_data
            save_accounts(accounts)
            st.success(f"✅ ₹{amount} deposited successfully!")

    elif action == "Withdraw":
        amount = st.number_input("💸 Enter withdrawal amount", min_value=0.0, step=0.01, key="withdraw")
        if st.button("🏧 Confirm Withdrawal"):
            if user_acc_data["balance"] >= amount:
                user_acc_data["balance"] -= amount
                user_acc_data["transactions"].append({
                    "type": "withdraw",
                    "amount": amount,
                    "balance": user_acc_data["balance"],
                    "timestamp": str(datetime.now())
                })
                accounts[str(acc_number)] = user_acc_data
                save_accounts(accounts)
                st.success(f"✅ ₹{amount} withdrawn successfully!")
            else:
                st.error("⚠️ Insufficient funds.")

    elif action == "Check Balance":
        st.info(f"📌 Your current balance is: **₹{user_acc_data['balance']:.2f}**")

    elif action == "Transaction History":
        txns = user_acc_data.get("transactions", [])
        if txns:
            df = pd.DataFrame(txns)
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            st.write("📜 Recent Transactions")
            st.dataframe(df)
            st.line_chart(df.set_index("timestamp")["balance"], use_container_width=True)
        else:
            st.info("📭 No transactions found.")

# ---------------------- Footer ---------------------- #
st.markdown("---")
st.caption("💡 Tip: Always logout when done. For feedback, email us at support@upbank.com")