from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", animation_class="start-home")


@app.route("/projects")
def projects():
    return render_template("projects.html", animation_class="start-projects")


@app.route("/contact")
def contact():
    return render_template("contact.html", animation_class="start-contact")


@app.route("/about")
def about():
    return render_template("about.html", animation_class="start-about")


if __name__ == "__main__":
    app.run(debug=True)
