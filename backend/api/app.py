from flask import Flask, jsonify, request
from userdata import *
app = Flask(__name__)

username = "Samikmalhotra"

@app.route("/", methods=['POST','GET'])
def index():

    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        username = json.username

        # return json with details
    try:
        user_data = getData(username)
        user =  jsonify(user_data)
    except:
        user = {"message": "username not found"}

        # check if the user is not an organization
    if check_if_org(username):
        trends = {"message": "organization not supported"}

    # return json with details
    try:
        trends_data = getTrends(username)
        trends = jsonify(trends_data)
    except:
        trends = {"message": "username not found"}

        # check if the user is not an organization
    if check_if_org(username):
        streak = {"message": "organization not supported"}
    
    # return json with details
    try:
        streak_data = getLongestStreakContributions(username)
        streak = jsonify(streak_data)
    except:
        streak = {"message": "username not found"}

        # check if the user is not an organization
    if check_if_org(username):
        return {"message": "organization not supported"}
    
    # return json with details
    try:
        lazygap_data = getLazyGap(username)
        lazygap = jsonify(lazygap_data)
    except:
        lazygap = {"message": "username not found"}

        # check if the user is not an organization
    if check_if_org(username):
        trend_month = {"message": "organization not supported"}
    
    # return json with details
    try:
        trend_month_data = monthDistribution(username)
        trend_month = jsonify(trend_month_data)
    except:
        trend_month = {"message": "username not found"}

    # check if the user is not an organization
    if check_if_org(username):
        trend_day = {"message": "organization not supported"}
    
    # return json with details
    try:
        trend_day_data = dayDistribution(username)
        trend_day = jsonify(trend_day_data)
    except:
        trend_day = {"message": "username not found"}

    # check if the user is not an organization
    if check_if_org(username):
        trends_fave_day = {"message": "organization not supported"}
    
    # return json with details
    try:
        trends_fave_day_data = fave_day(username)
        trends_fave_day = jsonify(trends_fave_day_data)
    except:
        trends_fave_day = {"message": "username not found"}

        # check if the user is not an organization
    if check_if_org(username):
        trends_bestday = {"message": "organization not supported"}
    
    # return json with details
    try:
        trends_bestday_data = best_day(username)
        trends_bestday = jsonify(trends_bestday_data)
    except:
        trends_bestday = {"message": "username not found"}




if __name__ == "__main__":
    app.run(debug=True)