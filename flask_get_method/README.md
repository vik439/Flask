# Flask Application Demonstrating GET Method

## Overview  
This Flask application demonstrates how to use the **GET HTTP method** to retrieve user information from a simulated database (Python dictionary). It provides an API route to fetch user details.

## Installation  
1. Clone this repository or create a new project folder.  
2. Install Flask using pip:  
   ```bash
   pip install flask
   ```
3. Run the application:  
   ```bash
   python app.py
   ```

## Project Structure  
```
/flask_get_app
│── app.py
└── README.md
```

## Usage  
### **1. Start the Flask Application**  
Once the application is running, it will be accessible at:  
```
http://127.0.0.1:5000/
```

### **2. Retrieve All Users (GET Request)**  
To fetch the list of users, send a **GET** request to:
```
http://127.0.0.1:5000/users
```
Example using **cURL**:
```bash
curl -X GET http://127.0.0.1:5000/users
```

 **Response Example:**
```json
{
  "users": [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
  ]
}
```

### **3. Retrieve a Specific User by ID (GET Request)**  
To fetch details of a specific user, send a **GET** request to:
```
http://127.0.0.1:5000/users/<user_id>
```
Example:
```bash
curl -X GET http://127.0.0.1:5000/users/1
```
📌 **Response Example:**
```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}
```

### **4. Error Handling**  
If the user ID does not exist, the response will be:
```json
{
  "error": "User not found"
}
```

## Features  
- Uses **Flask** to create a simple REST API.  
- Implements the **GET method** to retrieve user information.  
- Supports retrieving **all users** or a **specific user by ID**.  
- Handles error cases when a user is not found.  

## License  
This project is open-source and free to use.

