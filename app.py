from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def loginpage():
  return("hello app")

@app.route("/home", methods=["POST","GET"])
def getdata():
  if session.get("cards") is None:
    session["cards"] = []
  if request.method == "POST":
    activity = request.form.get("card")
    session["cards"].append(activity)
  return(render_template('layout.html', cards=session["cards"]))
