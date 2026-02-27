# app/user_service.py

import sqlite3
import os
from flask import Flask, request

app = Flask(__name__)

DATABASE = "users.db"

# environment variables
API_SECRET = "super-secret-key-123"

@app.route("/user")
def get_user():
    username = request.args.get("username")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Vulnerable to SQL Injection
    query = "SELECT * FROM users WHERE username = '%s'" % username
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()

    return {"data": result}


@app.route("/ping")
def ping():
    host = request.args.get("host")

    # Vulnerable to Command Injection
    os.system(f"ping -c 1 {host}")

    return {"status": "pinged"}

@app.route("/activity") #define a new route '/activity' to handle user activity requests
def activity():
    username = request.args.get("actions")
    if username != API_SECRET:
        return {"error": "Unauthorized"}, 401
    # Simulate fetching user activity
    activity = [
        {"action": "login", "timestamp": "2024-01-01T12:00:00Z"},
        {"action": "viewed_profile", "timestamp": "2024-01-01T12:05:00Z"},
        {"action": "logout", "timestamp": "2024-01-01T12:10:00Z"},
    ]
    return {"activity": activity}


if __name__ == "__main__":
    app.run(debug=True)