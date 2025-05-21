from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated in-memory database
users = []

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()

    # ✅ FIX: Only allow specific fields. Do not accept is_admin from client.
    new_user = {
        "username": data.get("username"),
        "email": data.get("email"),
        "password": data.get("password"),  # Ideally hashed in real app
        "is_admin": False  # Default only — can't be set by user
    }

    users.append(new_user)
    return jsonify({"message": "User registered", "user": new_user}), 201

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

if __name__ == "__main__":
    app.run(debug=True, port=5002)