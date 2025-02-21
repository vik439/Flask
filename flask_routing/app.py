from flask import Flask

app = Flask(__name__)

# Static Routing: Fixed routes that do not change

@app.route('/')
def home():
    return "<h1>Welcome to the Home Page</h1><p>This is a static route.</p>"

@app.route('/about')
def about():
    return "<h1>About Us</h1><p>Learn more about our application.</p>"

@app.route('/contact')
def contact():
    return "<h1>Contact Us</h1><p>Feel free to reach out!</p>"

# Dynamic Routing: Routes that accept parameters

@app.route('/user/<username>')
def user_profile(username):
    return f"<h1>Welcome, {username}!</h1><p>This is your profile page.</p>"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"<h1>Post ID: {post_id}</h1><p>This is a dynamic route for displaying post details.</p>"
@app.route('/product/<string:product_name>')
def product_page(product_name):
    return f"<h1>Product: {product_name}</h1><p>Details about {product_name} will be shown here.</p>"

if __name__ == '__main__':
    app.run(debug=True)
