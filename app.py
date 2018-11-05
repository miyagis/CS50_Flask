# "application.py" is the common name for Flask

from flask import Flask, render_template

# create a new flask app
app = Flask(__name__)

# route: part of the URL which determines which pages you request
# slash is the default page of the website
# when the user goes to my main page (with just slash) the run the index function
@app.route("/")
def main():
    headline = "var test"
    return render_template("main.html", headline=headline)

@app.route("/<string:name>")
def hello(name):
    zin = "<h1>hi {}</h1>".format(name)
    return zin
