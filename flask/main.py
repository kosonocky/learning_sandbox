from cProfile import run
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def display_welcome():
    return f"""
    <h1>Welcome</h1><a href='/profile'>Click Here to go to profile</a>
    """


@app.route("/profile")
def display_profile():
    return f"""
    <h1>My name is Clay and I am the only person who exists in local host port 5000!</h1><a href='/'>Click here if you want to return to the welcome page</a>
    """


if __name__ == '__main__':
    app
