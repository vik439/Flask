from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route to Serve Media Files (Uploads)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    app.run(debug=True)
