from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)

