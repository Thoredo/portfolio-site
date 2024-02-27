from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Email
from datetime import datetime
from dotenv import load_dotenv
import os
import smtplib
import json

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


class ContactForm(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    email = EmailField("Email:", validators=[DataRequired(), Email()])
    message = TextAreaField("Message:", validators=[DataRequired()])
    submit = SubmitField("Submit")


def send_mail(name, email, message):
    from_addr = "jurgenst@jurgen-stegeman-portfolio.nl"
    server = smtplib.SMTP('nl1-ss104.a2hosting.com', 587)
    server.login(from_addr, os.getenv("PASSWORD"))
    to_addr = "jurgenst@jurgen-stegeman-portfolio.nl"

    email_message = f"{name}, sent you the following message: \n{message}"
    
    print(from_addr)
    print(to_addr)
    print(email_message)

    text = f"Subject: Message from { email }\n\n{email_message}"
    
    print(text)

    server.sendmail(from_addr, to_addr, text)
    print(test)
    server.quit()


def calculate_age(birthdate):
    today = datetime.today()
    age = (
        today.year
        - birthdate.year
        - ((today.month, today.day) < (birthdate.month, birthdate.day))
    )
    return age


with open("static/data/projects.json") as file:
    project_data = json.load(file)


@app.route("/")
def index():
    return render_template("index.html", animation_class="start-home")


@app.route("/projects")
def projects():
    return render_template(
        "projects.html", animation_class="start-projects", project_data=project_data
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    # User input
    name = None
    email = None
    message = None
    form = ContactForm()
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        email = form.email.data
        form.email.data = ""
        message = form.message.data
        form.message.data = ""

        send_mail(name, email, message)

    return render_template(
        "contact.html",
        animation_class="start-contact",
        name=name,
        form=form,
        email=email,
        message=message,
    )


@app.route("/about")
def about():
    birthdate = datetime(1989, 10, 4)
    age = calculate_age(birthdate)
    birthdate_nova = datetime(2021, 4, 26)
    age_nova = calculate_age(birthdate_nova)
    return render_template(
        "about.html", animation_class="start-about", age=age, age_nova=age_nova
    )


@app.route("/project/<string:name>")
def show_project(name):
    requested_project = None
    for project in project_data:
        if project["project-name"] == name:
            requested_project = project
    return render_template("project.html", project=requested_project)


if __name__ == "__main__":
    app.run(debug=True)
