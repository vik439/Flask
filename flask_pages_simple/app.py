from flask import Flask

app = Flask(__name__)  # Initialize the Flask app

# Home Page Route
@app.route('/')
def home():
    return "<h1>Welcome to the Home Page</h1><p>This is the main page.</p>"

# About Page Route
@app.route('/about')
def about():
    return "<h1>About Us</h1><p>Learn more about our application.</p>"

# Contact Page Route
@app.route('/contact')
def contact():
    return "<h1>Contact Us</h1><p>Feel free to reach out!</p>"

if __name__ == '__main__':
    app.run(debug=True)  # Run the application in debug mode
