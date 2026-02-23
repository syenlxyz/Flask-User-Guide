from flask import Flask

app = Flask(__name__)

from flask import request, render_template

def do_the_login():
    return 'Login Successful'

def show_the_login_form():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.get('/login2')
def login_get():
    return show_the_login_form()

@app.post('/login2')
def login_post():
    return do_the_login()