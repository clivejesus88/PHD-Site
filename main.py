from flask import Flask, render_template, url_for , redirect, request, flash
from flask_mailman import EmailMessage, Mail
from dotenv import load_dotenv
import os

load_dotenv()

# Serve static files from the templates folder (existing project structure)

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME", "maileasy031@gmail.com")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD", "qrzxcztuawjyeeng")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "cajfuxvisglybstg")
mail = Mail(app)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/contact', methods=['GET',"POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        msg = EmailMessage(subject=f"{subject}",
                      from_email=f"{name} <{email}>",
                      to=[app.config['MAIL_USERNAME']])
        msg.body = f"From: {name}\nEmail: {email}\n\n{message}"
        msg.send()
        flash('Message sent successfully!')
        return redirect(url_for('contact'))
    return render_template('contact.html')


@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)