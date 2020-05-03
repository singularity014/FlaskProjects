from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Flask Obj
app = Flask(__name__)
# config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///debDB_test.sqlite'
db = SQLAlchemy(app)

# owner

class Surveyparams(db.Model):
    survey_id = db.Column(db.Integer, primary_key=True)
    initiator = db.Column(db.String(50), nullable=False)
    initiator_email = db.Column(db.String(120), nullable=False)
    survey_reason = db.Column(db.String(120), nullable=False)
    survey_date = db.Column(db.String(30), nullable=False)
    polls = db.relationship('Poll', backref=db.backref('surveyparams'))



# pet

class Poll(db.Model):
    poll_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    answer_1 = db.Column(db.String(120))
    answer_2 = db.Column(db.String(120))

    survey_id = db.Column(db.Integer, db.ForeignKey('surveyparams.survey_id'))




