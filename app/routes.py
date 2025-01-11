# imports
from main import app, render_template

# routes
@app.route("/")
def index():
    return render_template("index.html", pageTitle = "Home")


@app.route("/portfolio/")
def portfolio():
    return render_template("portfolio.html", pageTitle = "Portfolio")


@app.route("/services/")
def services():
    return render_template("services.html", pageTitle = "Sevices")


@app.route("/about/")
def about():
    return render_template("about.html", pageTitle = "About us")
    

@app.route("/blog/")
def blog():
    return render_template("blog.html", pageTitle = "Blog")


@app.route("/contact/")
def contact():
    return render_template("contact.html", pageTitle = "Contact")