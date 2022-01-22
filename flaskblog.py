from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World123!</p>"


@app.route("/about")
def about():
    return "<p>About</p>"

if __name__ == '__main__':
    app.run(debug=True)

