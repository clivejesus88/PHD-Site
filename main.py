from flask import Flask, render_template, url_for

# Serve static files from the templates folder (existing project structure)
app = Flask(__name__, static_folder='templates', static_url_path='/static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/causes')
def causes():
    return render_template('causes.html')

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

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)