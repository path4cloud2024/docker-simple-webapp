import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to Path4Cloud trainings"

@app.route("/courses")
def hello():
    return "We provide all DevOps tools and trainings as per real IT Industry standard"

if __name__ == "__main__":
    app.run()