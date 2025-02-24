from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Home Page with Flash Messages
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            flash("Error: Name cannot be empty!", "error")
        else:
            flash(f"Success: Welcome, {name}!", "success")
            return redirect(url_for('success', name=name))
    
    return render_template('index.html')

# Success Page
@app.route('/success/<name>')
def success(name):
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
