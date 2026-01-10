from flask import Flask, render_template, url_for, redirect, request, flash
from flask_mailman import Mail, EmailMessage
from dotenv import load_dotenv
import os

# from queue_email import email_queue
# from tasks import send_contact_email

load_dotenv()

app = Flask(__name__)

# --------------------
# Configuration
# --------------------
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

# --------------------
# Routes
# --------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/programs")
def programs():
    return render_template("programs.html")


@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        if not all([name, email, subject, message]):
            flash("All fields are required.", "danger")
            return redirect(url_for("contact"))

        # Queue email instead of sending directly
        with app.app_context():
            msg = EmailMessage(
            subject=subject,
            from_email=f"{name} <{email}>",
            to=['phdfamilynetworkinternational@gmail.com'],
        )

            msg.body = f"""
From: {name}
Email: {email}

Message:
{message}
"""
            msg.send()


        flash("Message sent successfully!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
