# Flask Application with Template Inheritance

## Overview  
This Flask application demonstrates **template inheritance** using **Jinja2**. It utilizes a base template (`base.html`) that includes common elements like headers and footers, while individual pages extend it to display unique content.

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

## Features  
- **Template Inheritance:** Uses a base template to maintain a consistent layout.  
- **Dynamic Content:** Each child template extends the base template and defines its own content.  
- **Easy Maintenance:** Common HTML structure is centralized in `base.html`.  

## License  
This project is open-source and free to use.  

