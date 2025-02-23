# Flask Application with SQLAlchemy

## Overview  
This Flask application demonstrates how to integrate **SQLAlchemy** with **Flask** to create and manage a SQLite database. It provides routes to add and list users stored in the database.

## Installation  
1. Clone this repository or create a new project folder.  
2. Install Flask and SQLAlchemy using pip:  
   ```bash
   pip install flask flask-sqlalchemy
   ```
3. Run the application:  
   ```bash
   python app.py
   ```

## Project Structure  
```
/flask_sqlalchemy_app
│── app.py
└── README.md
```

## Configuration  
- The application uses **SQLite** as the database.  
- The database file (`example.db`) is stored locally.
- SQLAlchemy is configured with:
  ```python
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  ```

## Usage  
### **1. Create and Initialize the Database**  
When you run `app.py`, Flask will create the database (`example.db`) and tables automatically using:
```python
with app.app_context():
    db.create_all()
```

### **2. Add a New User**  
To add a new user, send a GET request to:
```
http://127.0.0.1:5000/add/<username>/<email>
```
Example:
```
http://127.0.0.1:5000/add/johndoe/john@example.com
```
📌 **Response:**
```
Added user johndoe with email john@example.com
```

### **3. List All Users**  
To retrieve a list of all users stored in the database, visit:
```
http://127.0.0.1:5000/users
```
📌 **Response Example:**
```json
{
  "users": ["johndoe", "janedoe"]
}
```

## Features  
- Uses **Flask-SQLAlchemy** for database integration.  
- Supports adding and retrieving users via API routes.  
- Automatically creates the SQLite database if it doesn't exist.  

## License  
This project is open-source and free to use.

s