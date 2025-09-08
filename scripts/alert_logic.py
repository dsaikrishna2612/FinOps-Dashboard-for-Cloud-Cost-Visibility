import sqlite3

conn = sqlite3.connect('database/finops.db')
cursor = conn.cursor()

cursor.execute("SELECT service, SUM(cost) FROM usage GROUP BY service")
rows = cursor.fetchall()

for service, total_cost in rows:
    if total_cost > 0.00:  # Replace with your free-tier threshold
        print(f"⚠️ Alert: {service} has exceeded free-tier usage with ₹{total_cost:.2f}")

conn.close()

