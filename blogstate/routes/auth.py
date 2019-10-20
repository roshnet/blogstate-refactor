from blogstate import app
from flask import (
    render_template,
    request
)


@app.route('/signin')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("auth/login.html")


@app.route('/join')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("auth/signup.html")
