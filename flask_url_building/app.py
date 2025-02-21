from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/redirect_home')
def redirect_home():
    return redirect(url_for('home'))  # Redirects to the home page

if __name__ == '__main__':
    app.run(debug=True)
