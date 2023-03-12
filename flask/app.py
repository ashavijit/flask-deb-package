from flask import Flask
import datetime
import platform

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/info")
def info():
    #color the output
    return "This is a Flask app running on " + platform.system() + "."

@app.route("/time")
def time():
    return "The current time is " + str(datetime.datetime.now()) + "."

if __name__ == "__main__":
    app.run(host='', port=8080)