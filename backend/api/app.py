
from flask import Flask, jsonify
from userdata import *
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def index():
    return "Welcome to the Github Visualizer"

@app.route("/<username>/")
@cross_origin()
def user(username):
    # return json with details
    if check_if_org(username):
        return {"message": "organization not supported"}

    try:
        data = getData(username)
        trends = getTrends(username)
        streak = getLongestStreakContributions(username)
        gap = getLazyGap(username)
        months = monthDistribution(username)
        current_months=monthDistributionCurrentYear(username)
        fav_day= fave_day(username)
        bestday= best_day(username)


        return jsonify(data, trends, streak, gap, months, current_months, fav_day, bestday)
    except:
        return {"message": "username not found"}
    

@app.route("/<username>/trends/")
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

@app.route("/<username>/streak/")
def streak(username):
    # check if the user is not an organization
    if check_if_org(username):
        return {"message": "organization not supported"}
    
    # return json with details
    try:
        data = getLongestStreakContributions(username)
        return jsonify(data)
    except:
        return {"message": "username not found"}

@app.route("/<username>/lazygap/")
def lazygap(username):
    # check if the user is not an organization
    if check_if_org(username):
        return {"message": "organization not supported"}
    
    # return json with details
    try:
        data = getLazyGap(username)
        return jsonify(data)
    except:
        return {"message": "username not found"}
@app.route("/<username>/trends/month/")
def trends_month(username):
    # check if the user is not an organization
    if check_if_org(username):
        return {"message": "organization not supported"}
    
    # return json with details
    try:
        data = monthDistribution(username)
        return jsonify(data)
    except:
        return {"message": "username not found"}
@app.route("/<username>/trends/day/")
def trends_day(username):
    # check if the user is not an organization
    if check_if_org(username):
        return {"message": "organization not supported"}
    
    # return json with details
    try:
        data = dayDistribution(username)
        return jsonify(data)
    except:
        return {"message": "username not found"}

@app.route("/<username>/trends/fave_day/")
def trends_fave_day(username):
    # check if the user is not an organization
    if check_if_org(username):
        return {"message": "organization not supported"}
    
    # return json with details
    try:
        data = fave_day(username)
        return jsonify(data)
    except:
        return {"message": "username not found"}
@app.route("/<username>/trends/bestday/")
def trends_bestday(username):
    # check if the user is not an organization
    if check_if_org(username):
        return {"message": "organization not supported"}
    
    # return json with details
    try:
        data = best_day(username)
        return jsonify(data)
    except:
        return {"message": "username not found"}
if __name__ == "__main__":
    app.run(debug=True)

