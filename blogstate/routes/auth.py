from blogstate import app


@app.route('/')
def home():
    return "ooo"


@app.route('/greet/<user>')
def greet(user):
    return f"Hello, {user}"
