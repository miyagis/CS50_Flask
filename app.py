# "application.py" is the common name for Flask

from flask import Flask, render_template, request, session
from flask_session import Session
import datetime
from random import randrange

# create a new flask app
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# route: part of the URL which determines which pages you request
# slash is the default page of the website
# when the user goes to my main page (with just slash) the run the index function

quotes = ["I can't believe you committed suicide. I cannot believe you committed suicide. How could you have done this? How could you have committed suicide?",
"I'm going to continue hacking into these government systems to see what I can find out.",
"Here are the files and supporting documents. And supporting truths. The factual documents.",
"I've been hacking into government and corporate systems all over the country. All over the world. I have discovered more information than any hacker ever has.",
"I don't know who that is!"]

def get_quote():
    i = randrange(len(quotes)-1)
    quote = quotes[i]
    quote = '"' + quote + '"'
    return quote

@app.route("/")
def main():
    page_title = "Main"
    return render_template("main.html", quote=get_quote(), page_title=page_title)

@app.route("/main")
def main_bis():
    page_title = "Main"
    return render_template("main.html", quote=get_quote(), page_title=page_title)

@app.route("/about")
def about():
    page_title = "About"
    return render_template("about.html", quote=get_quote(), page_title=page_title)

@app.route("/twisted_pair")
def twisted_pair():
    page_title = "Twisted Pair"
    return render_template("twisted_pair.html", quote=get_quote(), page_title=page_title)

@app.route("/pass_thru")
def pass_thru():
    page_title = "Pass Thru"
    return render_template("pass_thru.html", quote=get_quote(), page_title=page_title)

@app.route("/contact")
def contact():
    page_title = "Contact"
    return render_template("contact.html", quote=get_quote(), page_title=page_title)

# --------------------TESTS-----------------------
# @app.route("/t2")
# def list_names():
#     names = ["Bart", "Roksana", "Kurwaman"]
#     return render_template("main.html", names=names, new_year=False)
#
# @app.route("/t4")
# def get_t4():
#     return render_template("test4.html")
#
# @app.route("/t3", methods=["POST"])
# def test4():
#     test = request.form.get("test")
#     test = test
#     return render_template("test4.html", test=test, mylist=mylist)
#
# @app.route("/t5", methods=["GET", "POST"])
# def test5():
#     if session.get("mylist") is None:
#         session["mylist"] = []
#     if request.method == "POST":
#         test = request.form.get("test")
#         session["mylist"].append(test)
#
#     return render_template("about.html", test=test, mylist=session["mylist"])
#
# @app.route("/t6")
# def main():
#     now = datetime.datetime.now()
#     # create a boolean variable which is True when 01.01
#     new_year = now.month == 1 and now.day == 1
#     return render_template("main.html", new_year=new_year)
# --------------------AFVAL-----------------------

# # Test 1
# @app.route("/t1_<string:name>")
# def hello(name):
#     zin = "<h1>hi {}</h1>".format(name)
#     return zin
