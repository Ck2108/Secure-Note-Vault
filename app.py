# Secure Note Vault - Complete Flask App (Beginner Friendly)

from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet
import sqlite3, os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "super-secret-key")  # Secret for session security

# Load or generate encryption key for Fernet
key = os.getenv("ENCRYPTION_KEY")
if not key:
    key = Fernet.generate_key().decode()
    print("Generated Encryption Key:", key)  # Print to save manually in your .env
fernet = Fernet(key.encode())

# Set up Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = str(id)
        self.username = username
        self.password = password

# Database helper

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Load user for session
@login_manager.user_loader
def load_user(user_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    if row:
        return User(row['id'], row['username'], row['password'])
    return None

@app.route("/")
def index():
    return redirect("/login")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        hashed_pw = generate_password_hash(password)

        conn = get_db()
        try:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Username already taken."
        return redirect("/login")
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user_row = cur.fetchone()

        if user_row and check_password_hash(user_row['password'], password):
            user = User(user_row['id'], user_row['username'], user_row['password'])
            login_user(user)
            return redirect("/dashboard")
        return "Invalid credentials"
    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes WHERE user_id = ?", (current_user.id,))
    notes = [fernet.decrypt(row['note']).decode() for row in cur.fetchall()]
    return render_template("dashboard.html", notes=notes)

@app.route("/add-note", methods=["POST"])
@login_required
def add_note():
    note = request.form['note']
    encrypted_note = fernet.encrypt(note.encode())

    conn = get_db()
    conn.execute("INSERT INTO notes (user_id, note) VALUES (?, ?)", (current_user.id, encrypted_note))
    conn.commit()
    return redirect("/dashboard")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)

