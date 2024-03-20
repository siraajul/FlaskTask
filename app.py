from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flasktask.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Flasktask(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/')
def hello_world():
    flasktask = Flasktask(title="FlaskTask", desc="Add Our FirstTask")
    db.session.add(flasktask)
    db.session.commit()
    return render_template('index.html')


@app.route('/show')
def products():
    alltasks = Flasktask.query.all()
    print(alltasks)
    return 'this is product page'


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)
