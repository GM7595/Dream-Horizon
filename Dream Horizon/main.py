from flask import Flask, render_template, url_for, redirect
from wtforms import Form, StringField, PasswordField, validators
import sqlalchemy

app = Flask(__name__)

# --------------------------------------------------- JOB DICTIONARY ---------------------------------------------------
job_list = [
    {
        "name": "個人投資家",
        "e_name": "Individual Investor",
        "img_path": "",
    },
    {
        "name": "サッカー選手",
        "e_name": "Football Player",
        "img_path": "",
    },
    {
        "name": "獣医師",
        "e_name": "Veterinary Physician",
        "img_path": "",

    },
    {
        "name": "理論物理学者",
        "e_name": "Physicist",
        "img_path": "",
    },
    {
        "name": "宇宙飛行士",
        "e_name": "Astronaut",
        "img_path": "",
    },
    {
        "name": "パイロット",
        "e_name": "Pilot",
        "img_path": "",
    },
    {
        "name": "映画監督",
        "e_name": "Movie Director",
        "img_path": "",
    },
    {
        "name": "建築家",
        "e_name": "Architect",
        "img_path": "",
    },
]
for loc, x in enumerate(job_list):
    x["loc"] = loc
print(job_list)

# ---------------------------------------------------- WTFORMS ---------------------------------------------------------


class LoginForm(Form):
    email = StringField('Email Address', [validators.Email("Not a valid email address"), validators.InputRequired(), validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.InputRequired(), validators.Length(min=6, max=35)])


class RegistrationForm(Form):
    username = StringField('Username', [validators.InputRequired(), validators.Length(max=25)])
    email = StringField('Email Address', [validators.Email("Not a valid email address"), validators.InputRequired(), validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.InputRequired(), validators.Length(min=6, max=35)])


# -------------------------------------------------- FRAMEWORK ---------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html", jobs=job_list)


@app.route("/jobs/<job_loc>")
def jobs(job_loc):
    return render_template("jobs.html", jobs=job_list[int(job_loc)])


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
