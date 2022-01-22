from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'a68cabeddf4b2d08ce3a10d2e758fb382f70d3fccb3b385b15b0495847354c0e'

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

