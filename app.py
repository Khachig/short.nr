import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' \
                                        + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)


# URL class/model
class URL(db.Model):
    short = db.Column(db.String(15), primary_key=True, autoincrement=False)
    long = db.Column(db.String, unique=True)
    timestamp = db.Column(db.Float)

    def __init__(self, short, long, timestamp):
        self.short = short
        self.long = long
        self.timestamp = timestamp

    def __repr__(self):
        return f'URL: {self.short}'
