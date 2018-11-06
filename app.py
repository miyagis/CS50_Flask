# "application.py" is the common name for Flask

from flask import Flask, render_template, request, session
from flask_session import Session
import datetime

# create a new flask app
app = Flask(__name__)

# route: part of the URL which determines which pages you request
# slash is the default page of the website
# when the user goes to my main page (with just slash) the run the index function
@app.route("/")
def main():
    now = datetime.datetime.now()
    # create a boolean variable which is True when 01.01
    new_year = now.month == 1 and now.day == 1
    return render_template("main.html", new_year=new_year)

# Test 1
@app.route("/t1_<string:name>")
def hello(name):
    zin = "<h1>hi {}</h1>".format(name)
    return zin

# Test 2
@app.route("/t2")
def list_names():
    names = ["Bart", "Roksana", "Kurwaman"]
    return render_template("main.html", names=names, new_year=False)

# Test 3
@app.route("/about")
def about():
    return render_template("about.html")

# # Test 4
# @app.route("/about", methods=["POST"])
# def test4():
#     test = request.form.get("test")
#     test = test
#     return render_template("test4.html", test=test, mylist=mylist)

# Test 5
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/about", methods=["GET", "POST"])
def test5():
    if session.get("mylist") is None:
        session["mylist"] = []
    if request.method == "POST":
        test = request.form.get("test")
        session["mylist"].append(test)

    return render_template("about.html", test=test, mylist=session["mylist"])
