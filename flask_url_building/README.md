# Flask Application with URL Building

## Overview  
This Flask application demonstrates **URL building** using `url_for()` to dynamically generate URLs and manage route changes efficiently. It also includes redirection using `redirect()`.

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
│── /templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
└── README.md
```

## Usage  
Once the application is running, visit the following URLs in your browser:  

- **Home Page:** [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/)  
- **About Page:** [`http://127.0.0.1:5000/about`](http://127.0.0.1:5000/about)  
- **Contact Page:** [`http://127.0.0.1:5000/contact`](http://127.0.0.1:5000/contact)  
- **Redirect Example:** [`http://127.0.0.1:5000/redirect_home`](http://127.0.0.1:5000/redirect_home)  

## Features  
- **Dynamic URL Building:** Uses `url_for()` to generate URLs dynamically.  
- **Redirection:** Redirects users to another route using `redirect()`.  
- **Template Inheritance:** Reuses a common base template (`base.html`) for a consistent layout.  
- **Navigation Links:** Dynamic navigation between pages.  

## License  
This project is open-source and free to use.  

