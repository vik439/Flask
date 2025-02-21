# Flask Application with Jinja2 Templating

## Overview  
This Flask application demonstrates how to **pass values and apply conditions** in an HTML page using **Jinja2 templating**. The application sends a dictionary and a list from the backend to the front-end, where they are dynamically rendered.

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
│   ├── index.html
└── README.md
```

## Usage  
Once the application is running, visit the following URL in your browser:  

- **Home Page:** [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/)

## Features  
- **Jinja2 Templating:** Dynamically render data in HTML templates.  
- **Passing Variables:** Flask sends a dictionary and a list to the template.  
- **Conditions in Templates:** Displays different content based on user role.  
- **Looping in Templates:** Iterates over a list to display dynamic content.  

## License  
This project is open-source and free to use.  

