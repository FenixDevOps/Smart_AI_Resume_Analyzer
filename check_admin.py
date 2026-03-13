import sqlite3
import os

db_path = os.path.join(os.getcwd(), "resume_data.db")

print("Using database:", db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# create admin table if missing
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT
)
""")

# remove old admin
cursor.execute("DELETE FROM admin")

# add new admin
cursor.execute(
    "INSERT INTO admin (email, password) VALUES (?, ?)",
    ("manigoud8885@gmail.com", "mani@123")
)

conn.commit()
conn.close()

print("Admin reset successfully")