# **Flask Mail Handling Example**  

## **Overview**  
This Flask application demonstrates how to send emails using **Flask-Mail**. It provides a simple **web interface** where users can enter a recipient’s email, subject, and message. The application then sends the email using **SMTP**.

---

## **Installation**  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/your-repo/flask-mail-app.git
cd flask-mail-app
```

### **Step 2: Install Flask-Mail**  
```bash
pip install Flask Flask-Mail
```

### **Step 3: Set Up Email Configuration**  
To send emails, configure your SMTP settings in **`app.py`**. Example settings for **Gmail SMTP**:

```
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your-email@gmail.com'
MAIL_PASSWORD = 'your-email-password'
MAIL_DEFAULT_SENDER = 'your-email@gmail.com'
```

🔹 **For security**, use an **App Password** instead of your real email password.  
🔹 **Environment variables** are recommended to store credentials securely.

---

## **Running the Flask Application**  

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and visit:
   - **Send Email Page:** [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/)  
   - Enter the recipient’s **email, subject, and message**, then click **Send Email**.  

---

## **Features**  
**Uses Flask-Mail to send emails** via SMTP.  
**Provides an HTML form** for email input.  
**Uses Flask flash messages** to display success or error messages.  
**Validates form input** (prevents empty fields).  
**Supports Gmail SMTP** and other email providers.  

---

## **Routes**  

| Route | Method | Description |
|--------|--------|-------------|
| `/` | `GET` | Displays the email form. |
| `/` | `POST` | Sends an email and shows a success/error message. |

---

## **Email Sending Process**  
1. **User enters recipient’s email, subject, and message.**  
2. **Flask-Mail sends the email** using SMTP.  
3. **Flash messages provide feedback** (success or error).  

---

## **Security Best Practices**  
- **Use an App Password** instead of your real email password.  
- **Store credentials using environment variables**.  
- **Never commit credentials** (`MAIL_USERNAME`, `MAIL_PASSWORD`) to GitHub.  

---

## **Enhancements**  
🔹 Add **logging** to track sent emails.  
🔹 Use **Bootstrap styling** for a better UI.  
🔹 Store sent emails in a **database** for tracking.  
