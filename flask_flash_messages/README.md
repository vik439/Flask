# **Flask Flash Messages Example with HTML Templates**  

## **Overview**  
This Flask application demonstrates how to use **flash messages** to display **success, error, or informational messages** after user interactions. Flash messages provide real-time feedback when a user submits a form.

---

## **Installation**  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/your-repo/flask-flash-messages.git
cd flask-flash-messages
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
/flask_flash_messages
│── app.py
│── /templates
│   ├── base.html
│   ├── index.html
│   ├── success.html
└── README.md
```

- `app.py` → Flask application handling **flash messages**.  
- `templates/base.html` → Base HTML template containing the **flash message section**.  
- `templates/index.html` → Main form page where the user enters their name.  
- `templates/success.html` → Page displaying a success message after submission.  
- `README.md` → Project documentation.  

---

## **Usage**  
Once the application is running, open your browser and visit:

- **Home Page (Form Page)** → [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/)  
  - Enter your name and submit the form.  
  - If the name is empty, a **red error message** appears.  
  - If the name is valid, a **green success message** appears, and the user is redirected to the success page.  

---

## **Features**  
 **Uses Flask's flash messages** for real-time feedback.  
 **Displays success and error messages dynamically**.  
 **Uses HTML templates for easy customization**.  
 **Implements template inheritance (`base.html`)** for modularity.  
 **Styled flash messages using CSS**.  

---

## **Routes**  

| Route | Method | Description |
|--------|--------|-------------|
| `/` | `GET` | Displays the form for user input. |
| `/` | `POST` | Processes form submission and flashes messages. |
| `/success/<name>` | `GET` | Displays a confirmation message. |

---

## **How Flash Messages Work in This Application**
1. **User submits the form**
   - If the name field is empty, an **error flash message** is displayed.
   - If the name is valid, a **success flash message** is displayed.
2. **Flash messages are retrieved in the base template (`base.html`)** using:
   ```html
   {% with messages = get_flashed_messages(with_categories=True) %}
   ```
3. **Messages are displayed inside a `<ul>` list** with appropriate styling.
4. **The user is redirected to a success page (`/success/<name>`)** if the submission is successful.

---

## ** Testing the Application**
### ** Valid Submission**
#### **Input:**
- Enter **"John"** in the form.
- Click **Submit**.

#### **Expected Result:**
- Redirects to `/success/John`.
- Displays the success message: **"Success: Welcome, John!"**.

---

### **Empty Submission**
#### **Input:**
- Leave the input field **empty**.
- Click **Submit**.

#### **Expected Result:**
- Displays a **red error message**: **"Error: Name cannot be empty!"**.
- Stays on the **same page** (does not redirect).

---
