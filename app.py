from flask import Flask, jsonify
from userdata import *
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Github Visualizer\nUser Basic Stats: http://localhost/<username>\nDay-to-Day trends: http://localhost/<username>/trends"

@app.route("/<username>")
def user(username):
    # return json with details
    try:
        data = getData(username)
        return jsonify(data)
    except:
        return {"message": "username not found"}

@app.route("/<username>/trends")
def trends(username):
    # check if the user is not an organization
    if check_if_org(username):
        return {"message": "organization not supported"}

    # return json with details
    try:
        data = getTrends(username)
        return jsonify(data)
    except:
        return {"message": "username not found"}
