from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Mail Configuration (Example: Using Gmail SMTP)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'example@gmail.com'
app.config['MAIL_PASSWORD'] = 'your password'  # Use environment variables for security
app.config['MAIL_DEFAULT_SENDER'] = 'example@gmail.com'

mail = Mail(app)

# Route to send email
@app.route('/', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        recipient = request.form['email']
        subject = request.form['subject']
        message_body = request.form['message']

        if not recipient or not subject or not message_body:
            flash("All fields are required!", "error")
        else:
            try:
                msg = Message(subject, recipients=[recipient], body=message_body)
                mail.send(msg)
                flash("Email sent successfully!", "success")
            except Exception as e:
                flash(f"Error: {str(e)}", "error")

        return redirect(url_for('send_email'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
