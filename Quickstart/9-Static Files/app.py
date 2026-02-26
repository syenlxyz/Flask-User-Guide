from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

from flask import url_for

with app.test_request_context():
    print(url_for('static', filename='style.css'))