from flask import Flask, redirect, url_for, render_template, request, flash, session
from datetime import timedelta
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
app.secret_key = "test"
app.permanent_session_lifetime = timedelta(minutes=15)

# Google Maps
app.config['GOOGLEMAPS_KEY'] = "AIzaSyCoMJFQnPrxQf4Y4XBmJIYmd0_ER0lncV4"

#Initialize etension
GoogleMaps(app)

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

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/maps")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=40.760648,
        lng=-111.871201,
        markers=[(40.760648, -111.871201)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=40.760648,
        lng=-111.871201,
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
    return render_template('maps.html', mymap=mymap, sndmap=sndmap)

if __name__=="__main__":
    app.run(debug=True)