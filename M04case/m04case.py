from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db=SQLAlchemy(app)

class Books(db.Model):
    id = db.collumn(db.Integer, primary_key=True)
    bookName = db.collumn(db.String(80),nullable=False)
    author = db.collumn(db.String(80),nullable=False)
    publisher = db.collumn(db.String(80),nullable=False)
    def __repr__(self):
        return f'{self.bookName}-{self.author}-{self.publisher}'

@app.route('/')
def index():
    return 'Hello'

@app.route('/books')
def getDrinks():
    return 'Books'
