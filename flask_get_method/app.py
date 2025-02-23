from flask import Flask, jsonify

app = Flask(__name__)

# Simulated database (dictionary)
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# GET Method - Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": [{"id": user_id, "name": user["name"], "email": user["email"]} for user_id, user in users.items()]})

# GET Method - Retrieve a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({"id": user_id, "name": user["name"], "email": user["email"]})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
