from flask import Flask, jsonify
from userdata import *
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Github Visualizer"

@app.route("/<username>")
def user(username):
    # return json with details
    print(username)
    try:
        #check if username is org
        if check_if_org(username):
            return {"message": "organzations not supported"}
    except:
        return {"message": "username not found"}
    try:
        profile_pic = get_image(username)
        number_of_commits = get_number_of_commits(username)
        return jsonify({"profile_pic": profile_pic, "number_of_commits": number_of_commits})
    except:
        return {"message": "username not found"}

