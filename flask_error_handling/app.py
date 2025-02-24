from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory database
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# Route to get user by ID with error handling
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        if user_id not in users:
            raise ValueError("User not found")  # Manually raising an exception
        return jsonify(users[user_id])
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

# Route to add a new user with error handling
@app.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.json
        if "name" not in data or "email" not in data:
            raise KeyError("Missing 'name' or 'email' field")
        
        new_id = max(users.keys(), default=0) + 1
        users[new_id] = {"name": data["name"], "email": data["email"]}
        return jsonify({"message": "User added", "user": users[new_id]}), 201
    except KeyError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

# Custom error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Custom error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
