# Secure-Note-Vault

Here you go! Below is a ✨ polished `README.md` for your **Secure Note Vault** project — filled with emojis, clear sections, and beginner-friendly highlights!

---

### ✅ Copy this into a file called `README.md` in your project folder:

````markdown
# 🔐 Secure Note Vault

A beginner-friendly, end-to-end encrypted **Flask-based password & note vault**, built using:
- 🧠 Python
- 🔐 Fernet (AES encryption)
- 🗄 SQLite (local DB)
- 🌐 Flask + Flask-Login (session management)
- 🌼 Cute HTML/CSS UI (for a better day)

---

## 🌟 Features

✅ Secure sign-up & login (with hashed passwords)  
✅ Encrypted note storage using `Fernet` (AES)  
✅ ✏️ Add secret notes from a clean, minimal dashboard  
✅ ⏰ Auto timestamping of saved notes  
✅ 🔒 User data isolation: see *your* notes only  
✅ 🎨 Styled login/signup/dashboard with fun emojis  
✅ 🧠 Beginner-friendly code and easy to customize

---

## 📷 Preview

> ✨ Cute, colorful, and functional UI for daily note-taking.

![App Screenshot](https://via.placeholder.com/700x400.png?text=Secure+Note+Vault+Preview)

---

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/Ck2108/Secure-Note-Vault.git
cd Secure-Note-Vault
````

### 2. Set up your virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
python init_db.py
```

### 5. Run the app

```bash
python app.py
```

🖥 Visit: `http://127.0.0.1:5000`

---

## 🛡 Security Details

* Passwords are hashed using `Werkzeug`’s `generate_password_hash`
* Notes are encrypted using `cryptography.fernet` (AES)
* Sessions secured using Flask `secret_key`
* CSRF protection and login guard via `Flask-Login`

---

## 💡 Ideas to Expand

* Add password strength check ✅
* Allow users to delete or edit notes
* Deploy to AWS EC2 (Free Tier!)
* Add email OTP verification
* Export notes to PDF or text

---

## 🧑‍💻 Author

Built with 💛 by [Chinmayee Kale](https://github.com/Ck2108)

---

## 📜 License

MIT License – Free to use, remix, and share!

---

## ✨ Contributions

Pull requests are welcome! Let’s secure notes, beautifully ✨

---
