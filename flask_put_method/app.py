from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database (dictionary)
users = {
    1: {"name": "Alice", "email": "alice@example.com"}
}

# PUT Method - Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    users[user_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"message": "User updated", "user": users[user_id]})

if __name__ == '__main__':
    app.run(debug=True)
