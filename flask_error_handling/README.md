# **Flask Exception & Error Handling Example**  

## **Overview**  
This is a simple **Flask API** that demonstrates how to handle **exceptions and errors** effectively. The application includes routes to:
- **Fetch a user** by ID (`GET`)
- **Add a new user** (`POST`)
- **Handle missing users, bad requests, and internal errors**
- **Use custom error handlers** for `404` (Not Found) and `500` (Internal Server Error)

This ensures that errors are handled gracefully, preventing crashes and returning useful responses.

---

## **Installation**  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/your-repo/flask-error-handling.git
cd flask-error-handling
```

### **Step 2: Install Flask**  
```bash
pip install flask
```

### **Step 3: Run the Flask Application**  
```bash
python app.py
```

---

## **Project Structure**  
```
/flask_error_handling
│── app.py
└── README.md
```

- `app.py` → Flask application handling **exceptions and errors**.
- `README.md` → Project documentation.

---

## **Usage**  

### **Fetch All Users (GET)**
#### **Request**
```bash
curl -X GET http://127.0.0.1:5000/users
```
#### **Response**
```json
{
    "1": {"name": "Alice", "email": "alice@example.com"},
    "2": {"name": "Bob", "email": "bob@example.com"}
}
```

---

### **Fetch a User by ID (GET)**
#### **Valid Request**
```bash
curl -X GET http://127.0.0.1:5000/users/1
```
#### **Response**
```json
{
    "name": "Alice",
    "email": "alice@example.com"
}
```

#### **Invalid Request (User Not Found)**
```bash
curl -X GET http://127.0.0.1:5000/users/100
```
#### **Response**
```json
{
    "error": "User not found"
}
```

---

### **Add a New User (POST)**
#### **Valid Request**
```bash
curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{"name": "Charlie", "email": "charlie@example.com"}'
```
#### **Response**
```json
{
    "message": "User added",
    "user": {
        "name": "Charlie",
        "email": "charlie@example.com"
    }
}
```

#### **Invalid Request (Missing Fields)**
```bash
curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{}'
```
#### **Response**
```json
{
    "error": "Missing 'name' or 'email' field"
}
```

---

### **Trigger a 404 Error (Invalid Route)**
```bash
curl -X GET http://127.0.0.1:5000/invalid-route
```
#### **Response**
```json
{
    "error": "Resource not found"
}
```

---

## **Features**
 **Handles exceptions and prevents application crashes**  
 **Provides user-friendly error messages**  
 **Custom error handlers for `404` and `500` errors**  
 **Ensures API responses are consistent**  

---

## **Routes**
| Route | Method | Description |
|--------|--------|-------------|
| `/users` | `GET` | Fetch all users. |
| `/users/<user_id>` | `GET` | Fetch a user by ID. |
| `/users` | `POST` | Add a new user. |

---


## **Error Handling Techniques**
### **1️ Try-Except Blocks**
- Used in `get_user()` and `add_user()` to catch:
  - **`ValueError`** for invalid user IDs.
  - **`KeyError`** for missing data in `POST` requests.

### **2️ Custom Error Handlers**
- `@app.errorhandler(404)`: Handles **"Not Found"** errors.
- `@app.errorhandler(500)`: Handles **"Internal Server Errors"**.

### **3️ Response Codes**
| Status Code | Meaning |
|-------------|---------|
| **200 OK** | Request was successful. |
| **201 Created** | A new user was successfully added. |
| **400 Bad Request** | Missing required fields in the request. |
| **404 Not Found** | The requested user or resource does not exist. |
| **500 Internal Server Error** | Something went wrong on the server. |

---
