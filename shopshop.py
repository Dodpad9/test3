from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///shopcat.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(512), nullable=False)

    def __repr__(self):
        return f"User {self.name} it email: {self.email}"


@app.route('/users')
def users():
    users = User.query.all()
    return f'{users}'


@app.route('/create_users')
def create_user():
    user = User(name='vova', email='nvdsjhvhj.com', password='123457')
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('users'))


with app.app_context():
    db.create_all()

app.run(debug=True)
