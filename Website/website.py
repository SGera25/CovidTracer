from flask import Flask, redirect, url_for, render_template, request, flash, session
from datetime import timedelta
import flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=15)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    age = db.Column(db.Integer(3))
    sex = db.Column(db.String(100))
    date = db.Column(db.String(100))
    time = db.Column(db.String(100))
    location = db.Column(db.String(100))
    mask = db.Column(db.String(100))
    symptoms =  db.Column(db.String(100))
    contact =  db.Column(db.String(100))

    def __init__(self, name, email, age, sex, date, time, location, mask, symptoms, contact):
        self.name = name
        self.email = email
        self.age = age
        self.sex = sex
        self.date = date
        self.time = time
        self.location = location
        self.mask = mask
        self.symptoms = symptoms
        self.contact = contact


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = requests.form["email"]
            session["email"] = email
        else:
            email = session["email"]
            if "email" in session:
                email = session["email"]

        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/map")
def map():
    return render_template("home.html")

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
