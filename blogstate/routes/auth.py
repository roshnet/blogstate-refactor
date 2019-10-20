from blogstate import app
from flask import render_template


@app.route('/signin')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("auth/login.html")


@app.route('/join')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("auth/signup.html")
