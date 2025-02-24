# Flask DELETE Method Example (REST API)

## Overview
This is a simple **Flask API** that demonstrates how to use the **DELETE method** to remove a user from an in-memory dictionary. The application provides an endpoint to **fetch all users** and another to **delete a specific user** using their ID.

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/flask-delete-api.git
cd flask-delete-api
```

### Step 2: Install Flask
```bash
pip install flask
```

### Step 3: Run the Application
```bash
python app.py
```

---

## Project Structure
```
/flask_delete_api
│── app.py
└── README.md
```

- `app.py` → Flask application handling the **DELETE method**.
- `README.md` → Project documentation.

---

## Usage
Once the application is running, open your browser or use **Postman/cURL** to test the API.

### **Get All Users (GET)**
#### **Request**
```bash
curl -X GET http://127.0.0.1:5000/users
```
#### **Response**
```json
{
    "1": {"name": "Alice", "email": "alice@example.com"},
    "2": {"name": "Bob", "email": "bob@example.com"},
    "3": {"name": "Charlie", "email": "charlie@example.com"}
}
```

---

### **Delete a User (DELETE)**
#### **Request**
```bash
curl -X DELETE http://127.0.0.1:5000/users/1
```

#### **Response (If user exists)**
```json
{
    "message": "User 1 deleted successfully"
}
```

#### **Response (If user not found)**
```json
{
    "error": "User not found"
}
```

---

## Features
Demonstrates Flask **DELETE method** using a REST API.  
**In-memory database (dictionary)** for easy testing.  
**Testable via Postman or cURL**.  
**Beginner-friendly Flask project** with minimal setup.  

---

## Routes
| Route | Method | Description |
|--------|--------|-------------|
| `/users` | `GET` | Fetch all users. |
| `/users/<user_id>` | `DELETE` | Deletes a user by ID. |

---

## Code Explanation

### **app.py**
- Starts a **Flask application**.
- Uses `GET` to **retrieve users** from an in-memory dictionary.
- Uses `DELETE` to **remove a user** based on ID.
- Returns appropriate **JSON responses**.

---

## License
This project is **open-source** and free to use.

