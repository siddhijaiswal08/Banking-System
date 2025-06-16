# Banking-System
# 🏦 UP Express Banking System

A modern, secure, and student-friendly **banking web app** built with **Python** and **Streamlit**, designed for university-level users to simulate a simplified banking system.

---

## 🚀 Features

- 🔐 **User Registration & Login** with password hashing
- 💰 **Savings and Current Account Options**
- 📈 **Banking Operations**: Deposit, Withdraw, Check Balance
- 📜 **Transaction History** with charts
- ✅ **Data Persistence** using JSON
- 🎨 Clean, minimal **light-themed UI**
- 💬 Emphasis on **security, compliance, and student-first design**

---

## 📸 UI Preview

![Homepage Screenshot](screenshots/homepage.png)
*Sample UI for home screen. Includes cards, alignment, and theme.*

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Backend logic and data handling |
| **Streamlit** | Web app interface |
| **JSON** | Local data storage for user accounts |
| **Pandas** | Transaction history and charting |
| **Hashlib** | Secure password hashing |

---

## 🧩 How It Works

- **Registration:** Users can create accounts by choosing account type, setting a password, and providing a deposit.
- **Login:** Secure login using account number and hashed password.
- **Dashboard:** Once logged in, users can:
  - Deposit or withdraw money
  - View real-time balance
  - See transaction history (tabular and graphical)
- **Data:** Stored in `accounts.json` for easy persistence without a database.

---

## 📦 Setup Instructions

### 1. Clone the Repository
<pre>
  ```bash
git clone https://github.com/siddhijaiswal08/Banking-System.git
cd up-express-banking ```
</pre>


### 2. Install Requirements
<pre>
   ```bash
pip install -r requirements.txt ``` 
</pre>

### 3. Run the App
<pre>
  streamlit run app.py
</pre>

 ### 📁 Project Structure
 up-express-banking/
│
├── app.py     # Main Streamlit app
├── accounts.json            # Stored user account data
├── requirements.txt         # List of dependencies
├── screenshots/             # UI screenshots
└── README.md                # This file

### 📧 Contact & Support
For feedback or support, please reach out at support@upbank.com


