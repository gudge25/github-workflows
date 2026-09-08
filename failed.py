import subprocess
import sqlite3

DB_PASSWORD = "admin123"  # hardcoded credential

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SQL injection: string-formatted query instead of parameterized
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

def ping_host(hostname):
    # Command injection: shell=True with unsanitized input
    result = subprocess.run(f"ping -c 1 {hostname}", shell=True, capture_output=True)
    return result.stdout

def divide(a, b):
    try:
        return a / b
    except:  # bare except swallows everything, including KeyboardInterrupt
        pass

def unused_function():
    x = 1
    y = 2  # unused variable
    return x
