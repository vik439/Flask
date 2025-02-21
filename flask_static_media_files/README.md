# Flask Application for Static and Media Files

## Overview  
This Flask application demonstrates how to serve **static files** (CSS, JavaScript, images) and **media files** like uploads.

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
│── /static
│   ├── css
│   │   ├── styles.css
│   ├── images
│   │   ├── logo.png
│   ├── js
│   │   ├── script.js
│── /uploads
│   ├── sample.pdf
│── /templates
│   ├── base.html
│   ├── index.html
└── README.md
```

## Usage  
Once the application is running, visit the following URLs in your browser:  

- **Home Page:** [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/)  
- **Download Media File:** [`http://127.0.0.1:5000/uploads/sample.pdf`](http://127.0.0.1:5000/uploads/sample.pdf)  

## Features  
- **Serving Static Files:** CSS, JavaScript, and images are loaded from the `/static` directory using `url_for()`.  
- **Serving Media Files:** The `/uploads` directory is used to serve downloadable files dynamically.  
- **Template Inheritance:** The app uses `base.html` as a common template for all pages.  
- **Navigation Support:** The app includes navigation for easier browsing.  

## License  
This project is open-source and free to use.  

