# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock user database (sensitive + non-sensitive)
users = {
    1: {
        "id": 1,
        "username": "alice",
        "email": "alice@example.com",
        "password_hash": "hashed_pw_123",
        "phone": "1234567890",
        "address": "123 Wonderland"
    },
    2: {
        "id": 2,
        "username": "bob",
        "email": "bob@example.com",
        "password_hash": "hashed_pw_456",
        "phone": "9876543210",
        "address": "456 Builder St"
    }
}

@app.route("/api/profile/<int:user_id>", methods=["GET"])
def get_profile(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

