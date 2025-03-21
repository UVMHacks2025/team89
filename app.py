from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, UTC
import requests
from sqlalchemy.sql.functions import user
from sqlalchemy import update

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

    if not(User.query.filter_by(username=name).first()):
        db.session.add(new_user)
        db.session.commit()
    else:
        print("EXISTING USER SELECTED")

    dummy_leaderboard = {'Norah22': 450, 'jordaniscool': 126, 'maya_studies': 788, 'leahlockedin': 439}
    for leaderboard_user in dummy_leaderboard.keys():
        if not(User.query.filter_by(username=leaderboard_user).first()):
            new_user = User(username = leaderboard_user, points = dummy_leaderboard[leaderboard_user], studying = "dummy")
            db.session.add(new_user)
            db.session.commit()

    top_users = User.query.order_by(User.points.desc()).limit(10).all()
    leaderboard_data = [{"username": user.username, "points": user.points} for user in top_users]

    payload = {
        'leaderboard': leaderboard_data,
    };

    print(payload)

    return jsonify(payload);

@app.route("/api/timerDone", methods=["POST"])
def timerDone():
    name = request.json["name"];

    user = User.query.filter_by(username=name).first()
    new_user = User(username=user.username, points=user.points + 100, studying=user.studying)

    db.session.delete(user)
    db.session.add(new_user)
    db.session.commit()

    top_users = User.query.order_by(User.points.desc()).limit(10).all()
    leaderboard_data = [{"username": user.username, "points": user.points} for user in top_users]

    payload = {
        'leaderboard': leaderboard_data,
    };

    return jsonify(payload);


with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(debug=True)


