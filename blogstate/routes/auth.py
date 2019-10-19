from blogstate import app
from flask import render_template


@app.route('/signin')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return f"Log In"


@app.route('/join')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return f"Sign Up"
