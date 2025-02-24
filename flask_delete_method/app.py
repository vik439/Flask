from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample database (dictionary)
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
    3: {"name": "Charlie", "email": "charlie@example.com"}
}

# Route to get all users (GET)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# DELETE Method - Remove a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": f"User {user_id} deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
