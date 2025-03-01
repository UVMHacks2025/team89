from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, UTC
import requests
import leaderboard
import timer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# db notes:
# columns in table for user info: username (pk), points, leaderboard index, achievements??, unlocked deco???
# columns in table for list: id (pk), task_name, task_description, task_priority, start_time, finish_time, username (fk)
class User(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    points = db.Column(db.Integer, nullable=False)
    studying = db.Column(db.String(80), nullable=False)
    #leaderboard_index = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(80), nullable=False)
    task_description = db.Column(db.String(80))
    task_priority = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.now(UTC))
    finish_time = db.Column(db.DateTime, default=datetime.now(UTC))
    username = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)
    def __repr__(self):
        return '<Task %r>' % self.task_name

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/api/start", methods=["POST"])
def start():
    name = request.json["name"];
    studying = request.json["studying"];
    print(f"[start] USER JOINED {name=} {studying=}")
    leaderboard.add_user(name)
    points = 0
    new_user = User(username=name, points=points, studying=studying)
    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        return 'there was an issue'

    payload = {
        'leaderboard': leaderboard.get_leaderboard(),
    };

    print(payload)

    return jsonify(payload);

with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(debug=True)


