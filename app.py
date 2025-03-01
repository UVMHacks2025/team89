from flask import Flask, render_template, request
import requests
import leaderboard
import timer

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/api/start", methods=["POST"])
def start():
    name = request.json["name"];
    studying = request.json["studying"];
    print(f"[start] USER JOINED {name=} {studying=}")
    leaderboard.add_user(name)
    print(leaderboard.get_leaderboard())
    return ""

@app.route("/api/start", methods=["POST"])
def count():
    print("Timer: ")
    timer.get_time()
    return ""

if __name__=="__main__":
    app.run(debug=True)


