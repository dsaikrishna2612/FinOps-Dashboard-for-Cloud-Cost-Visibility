import sqlite3

conn = sqlite3.connect('database/finops.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usage (
    date TEXT,
    service TEXT,
    cost REAL
)
''')

conn.commit()
conn.close()

