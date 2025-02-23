# Flask Application Demonstrating PUT Method

## Overview  
This Flask application demonstrates how to use the **PUT HTTP method** to update an existing user in a simulated database (Python dictionary). It provides an API route that allows updating user details via a JSON request.

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
/flask_put_app
│── app.py
└── README.md
```

## Usage  
### **1. Start the Flask Application**  
Once the application is running, it will be accessible at:  
```
http://127.0.0.1:5000/
```

### **2. Update an Existing User (PUT Request)**  
To update a user, send a **PUT** request with JSON data to:
```
http://127.0.0.1:5000/users/<user_id>
```
Example:
```bash
curl -X PUT http://127.0.0.1:5000/users/1 \
     -H "Content-Type: application/json" \
     -d '{"name": "Alice Updated", "email": "alice.updated@example.com"}'
```

 **Response Example:**
```json
{
  "message": "User updated",
  "user": {
    "name": "Alice Updated",
    "email": "alice.updated@example.com"
  }
}
```

### **3. Error Handling**  
If the user ID does not exist, the response will be:
```json
{
  "error": "User not found"
}
```

## Features  
- Uses **Flask** to create a simple REST API.  
- Implements the **PUT method** to update user information.  
- Handles error cases when a user is not found.  

## License  
This project is open-source and free to use.

