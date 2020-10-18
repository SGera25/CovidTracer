from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_googlemaps import GoogleMaps, Map
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config["SECRET_KEY"] = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.sqlite3"
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

list_of_markers = []

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    age = db.Column(db.String(3), unique=True)
    sex = db.Column(db.String(8), unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField("Remember me")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email(message="Invalid email"), Length(max=50)])
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=80)])

class SurveyInput(FlaskForm):
    name = StringField("Name (first and last)", validators=[InputRequired(), Length(min=0, max=30)])
    age = StringField("Age", validators=[InputRequired(), Length(min=1, max=2)])
    sex = PasswordField("Biological sex (m or f)", validators=[InputRequired(), Length(min=1, max=1)])

# Google Maps
app.config['GOOGLEMAPS_KEY'] = "AIzaSyCoMJFQnPrxQf4Y4XBmJIYmd0_ER0lncV4"

#Initialize etension
GoogleMaps(app)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for("dashboard"))
        return "<h1>Invalid username or password</h1>"

    return render_template("login.html", form=form)

@app.route('/signup', methods=["POST", "GET"])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>New user has been created!</h1>'
    return render_template("signup.html", form=form)

@app.route("/dashboard", methods=["POST", "GET"])
@login_required
def dashboard():
    form = SurveyInput()

    if form.validate_on_submit():
        new_survey = Survey(name=form.name.data, age=form.age.data, sex=form.sex.data)
        db.session.add(new_survey)
        db.session.commit()
        return '<h1>New survey has been submitted!</h1>'

    return render_template("dashboard.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/maps")
def mapview():
    # Creating map
    sndmap = Map(
        identifier="sndmap",
        lat=40.760648,
        lng=-111.871201,
        zoom=15,
        style="height:900px;width:900px;margin:30;",
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 40.759928,
             'lng': -111.875747,
             'infobox': "<b>Smith's</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 40.760948,
             'lng': -111.873592,
             'infobox': "<b>Jimmy John's</b>"
          }
        ]
    )
    return render_template('maps.html', sndmap=sndmap)

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
