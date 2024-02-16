from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


def calculate_age(birthdate):
    today = datetime.today()
    age = (
        today.year
        - birthdate.year
        - ((today.month, today.day) < (birthdate.month, birthdate.day))
    )
    return age


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
    birthdate = datetime(1989, 10, 4)
    age = calculate_age(birthdate)
    birthdate_nova = datetime(2021, 4, 26)
    age_nova = calculate_age(birthdate_nova)
    return render_template(
        "about.html", animation_class="start-about", age=age, age_nova=age_nova
    )


if __name__ == "__main__":
    app.run(debug=True)
