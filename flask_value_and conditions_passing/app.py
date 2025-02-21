from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = {"name": "John Doe", "role": "admin"}
    numbers = [1, 2, 3, 4, 5]
    return render_template('index.html', user=user, numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True)
