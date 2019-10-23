"""
Configures everything for the dashboard.
"""

from blogstate import app


# [WIP] TODO: Add routes and definitions

@app.route('/<username>/dashboard')
def dashboard(username):
    return ''
