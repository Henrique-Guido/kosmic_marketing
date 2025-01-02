from main import app, render_template

#routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")