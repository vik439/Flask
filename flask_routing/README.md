# Flask Application with Static and Dynamic Routing

## Overview  
This Flask application demonstrates **static routing** (fixed URLs) and **dynamic routing** (URLs with parameters). It allows users to navigate between pages with predefined and dynamic routes.

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
/flask_app
│── app.py
└── README.md
```

## Usage  
Once the application is running, visit the following URLs in your browser:  

### **Static Routes (Fixed URLs)**  
- **Home Page:** [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/)  
- **About Page:** [`http://127.0.0.1:5000/about`](http://127.0.0.1:5000/about)  
- **Contact Page:** [`http://127.0.0.1:5000/contact`](http://127.0.0.1:5000/contact)  

### **Dynamic Routes (URLs with Parameters)**  
- **User Profile Page:** [`http://127.0.0.1:5000/user/john`](http://127.0.0.1:5000/user/john) (Replace "john" with any username)  
- **Blog Post Page:** [`http://127.0.0.1:5000/post/10`](http://127.0.0.1:5000/post/10) (Replace "10" with any post ID)  
- **Product Page:** [`http://127.0.0.1:5000/product/laptop`](http://127.0.0.1:5000/product/laptop) (Replace "laptop" with any product name)  

## Features  
- Flask-based web application  
- Static routes for predefined pages  
- Dynamic routes for user profiles, blog posts, and product details  
- Simple and lightweight application structure  

## License  
This project is open-source and free to use.  

