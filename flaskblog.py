from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a68cabeddf4b2d08ce3a10d2e758fb382f70d3fccb3b385b15b0495847354c0e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

    # one to many relationship


data = [
    {
        'author' : 'Jane Doe',
        'title' : 'Blog post 1',
        'content' : 'first post content',
        'date' : 'Jan 22'
    },
        {
        'author' : 'Jane Doe',
        'title' : 'Blog post 2',
        'content' : 'second post content',
        'date' : 'Jan 22'
    }
]


@app.route("/")
def hello_world():
    return render_template('home.html', posts=data)

@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)

