
# Flask POST Method Example with HTML Form

## Overview
This is a simple **Flask web application** that demonstrates how to use the **POST method** to submit a form. The application includes an **HTML form** where users can enter their name, and upon submission, the application processes the input and displays a personalized message.

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/flask-post-form.git
cd flask-post-form
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
/flask_post_form
│── app.py
│── /templates
│   ├── form.html
│   ├── result.html
└── README.md
```

- `app.py` → Flask application file handling the **POST request**.
- `templates/form.html` → HTML form for user input.
- `templates/result.html` → Displays submitted user input.
- `README.md` → Project documentation.

---

## Usage
Once the application is running, open your browser and visit:

- **Form Page (GET & POST):** [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/)

### How It Works:
1. **GET Request**: The user accesses the form page.
2. **POST Request**: The user submits their name.
3. **Server Processes Data**: The application renders a new page displaying the entered name.

---

## Features
Demonstrates Flask **POST method** with HTML form.  
**No JSON required** – Uses traditional form submission.  
**Simple template rendering** using Flask’s `render_template()`.  
**Beginner-friendly Flask application** with minimal setup.  

---

## Routes
| Route | Method | Description |
|--------|--------|-------------|
| `/` | `GET` | Displays the form for user input. |
| `/` | `POST` | Processes form submission and displays input. |

---

## Code Explanation

### **app.py**
- Starts a **Flask application**.
- Uses `GET` to **render** `form.html` (displays the input form).
- Uses `POST` to **process form submission** and render `result.html`.

### **form.html**
- Contains an **input field** for the user to enter their name.
- Uses the **POST method** to send data to `/`.

### **result.html**
- Displays a **welcome message** using the submitted name.
- Includes a **"Go Back"** button to return to the form.

---

## License
This project is **open-source** and free to use.

