import sqlite3
conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS users")
c.execute("DROP TABLE IF EXISTS notes")
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)")
c.execute("""
    CREATE TABLE notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        note TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()
conn.close()

