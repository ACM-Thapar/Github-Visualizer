import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import calendar
# get data from github profile

class UserData:
    def __init__(self, username, profile_pic, followers, following, number_of_repos, name, bio, start_date, last_activity, github_link, number_gists, total_contributions, trends):
        self.username = username
        self.profile_pic = profile_pic
        self.followers = followers
        self.following = following
        self.number_of_repos = number_of_repos
        self.name = name
        self.bio = bio
        self.start_date = start_date
        self.last_activity = last_activity
        self.github_link = github_link
        self.number_gists = number_gists
        self.totalContributions = total_contributions
        self.trends = trends

    def jsonify(self):
        return {
            "username": self.username,
            "profile_pic": self.profile_pic,
            "followers": self.followers,
            "following": self.following,
            "number_of_repos": self.number_of_repos,
            "name": self.name,
            "bio": self.bio,
            "start_date": self.start_date,
            "last_activity": self.last_activity,
            "github_link": self.github_link,
            "number_gists": self.number_gists,
            "number_of_commits": self.totalContributions,
            #"trends": self.trends
        }

def get_image(username):
    url = "https://avatars.githubusercontent.com/" + username
    profile_pic = requests.get(url)
    if profile_pic.status_code == 200:
        return url
    else:
        return None

def get_number_of_commits(username):
    url = "https://github.com/" + username
    # scrape the html to get the number of commits in the last year
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    # find f4 text-normal mb-2 class
    commits = soup.find_all(class_="f4 text-normal mb-2")[0].get_text()
    number_commits = commits.split("\n")

    #flush the whitespaces
    number_commits = [x.strip() for x in number_commits][1]
    try:
        number_commits = int(number_commits)
    except:
        number_commits = 0
    return number_commits

def check_if_org(username):
    url = "https://api.github.com/users/" + username
    # get the json data
    json_data = requests.get(url).json()
    # check if the user is an organization
    if json_data["type"] == "Organization":
        return True
    else:
        return False

def get_number_of_followers(username):
    url = "https://api.github.com/users/" + username
    # get the json data
    json_data = requests.get(url).json()
    return json_data


def getData(username):
    if check_if_org(username):
        return {"message": "Organisations not supported"}
    else:
        url = "https://api.github.com/users/" + username
        json_data = requests.get(url).json()
        # get the number of followers
        followers = json_data["followers"]
        # get the number of following
        following = json_data["following"]
        # get the number of repos
        number_of_repos = json_data["public_repos"]
        # get the name
        name = json_data["name"]
        # get the bio
        bio = json_data["bio"]
        # get the start date
        start_date = json_data["created_at"]
        # get the last activity
        last_activity = json_data["updated_at"]
        # get the github link
        github_link = json_data["html_url"]
        # get the profile pic
        profile_pic = json_data["avatar_url"]
        # get the number of commits
        number_commits = get_number_of_commits(username)
        # number of gists
        number_gists = json_data["public_gists"]

        trends = getTrends(username)

        user_data = UserData(username, profile_pic, followers, following, number_of_repos, name, bio, start_date, last_activity, github_link, number_gists, get_number_of_commits(username), trends)
        return user_data.jsonify()


def getTrends(username):
    url = "https://github.com/" + username
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    non_commit_trends =  []
    commit_activity = soup.find_all("rect", class_="ContributionCalendar-day")
    for activity in commit_activity:
        # check those tags if they have data-date in them else ignore
        if "data-date" in str(activity) and "data-count" in str(activity):
            # get the date
            date = activity["data-date"]
            # get the number of commits
            if activity["data-count"] != "0":
                # add to the dictionary
                non_commit_trends.append({"date": date, "activity": int(activity["data-count"])})
    return non_commit_trends

def getNonWorkTrends(username):
    url = "https://github.com/" + username
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    non_commit_trends =  []
    commit_activity = soup.find_all("rect", class_="ContributionCalendar-day")
    for activity in commit_activity:
        # check those tags if they have data-date in them else ignore
        if "data-date" in str(activity) and "data-count" in str(activity):
            # get the date
            date = activity["data-date"]
            # get the number of commits
            if activity["data-count"] == "0":
                # add to the dictionary
                non_commit_trends.append(date)
    return non_commit_trends

def getLongestStreakContributions(username):
    trends = getTrends(username)
    
    # date format is YYYY-MM-DD
    # get the longest streak
    current_date = None
    longest_streak = {}
    date_range = []
    for trend in trends:
        if current_date == None:
            current_date = trend["date"]
            date_range.append({"start_date": current_date, "end_date": current_date, "count": 1, "commit_count": trend["activity"]})
        else:
            if trend["date"] == current_date:
                date_range[-1]["count"] += 1
                date_range[-1]["end_date"] = trend["date"]
                date_range[-1]["commit_count"] += trend["activity"]
            else:
                current_date = trend["date"]
                date_range.append({"start_date": current_date, "end_date": current_date, "count": 1, "commit_count": trend["activity"]})

            # increment the current_date
            current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
            current_date = current_date + datetime.timedelta(days=1)
            current_date = current_date.strftime("%Y-%m-%d")
    
    # get the max count dictionary
    max_count = max(date_range, key=lambda x: x["count"])
    return max_count

def getLazyGap(username):
    non_commit_trends = getNonWorkTrends(username)
    # get the longest streak
    current_date = None
    longest_streak = {}
    date_range = []
    for trend in non_commit_trends:
        if current_date == None:
            current_date = trend
            date_range.append({"start_date": current_date, "end_date": current_date, "gap": 1})
        else:
            if trend == current_date:
                date_range[-1]["gap"] += 1
                date_range[-1]["end_date"] = trend
            else:
                current_date = trend
                date_range.append({"start_date": current_date, "end_date": current_date, "gap": 1})

            # increment the current_date
            current_date = datetime.datetime.strptime(current_date, "%Y-%m-%d")
            current_date = current_date + datetime.timedelta(days=1)
            current_date = current_date.strftime("%Y-%m-%d")
    # get max
    max_count = max(date_range, key=lambda x: x["gap"])
    print(max_count)
    return max_count

def monthDistribution(username):
    trends = getTrends(username)
    months = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
    distribution = []
    """
    [
        {
            "month": "January",
            "commit_count": 0,
            "days": 0
        }
    ]
    """
    month_list = []
    for trend in trends:
        # get current year
        current_year = datetime.date.today().strftime("%Y")

        # make sure its the current year trend only
        if trend["date"].split("-")[0] != current_year:
            continue
        # get the month
        month = trend["date"].split("-")[1]
        # get the commit count
        commit_count = trend["activity"]
        # check if month is in the list
        if month not in month_list:
            month_list.append(month)
            distribution.append({"month": months[month], "commit_count": commit_count, "days": 1})
        else:
            # get the index of the month
            index = month_list.index(month)
            # increment the commit count
            distribution[index]["commit_count"] += commit_count
            distribution[index]["days"] += 1
    return distribution

def getDay(date):
    day = datetime.datetime.strptime(date, "%Y-%m-%d").weekday()
    return (calendar.day_name[day])

def dayDistribution(username):
    trends = getTrends(username)
    distribution = []
    """
    [
        {
            "day": "Monday",
            "commit_count": 0,
            "days": 0
        }
    ]
    """
    day_list = []
    for trend in trends:
        day = getDay(trend["date"])
        # get current year
        current_year = datetime.date.today().strftime("%Y")

        # make sure its the current year trend only
        if trend["date"].split("-")[0] != current_year:
            continue
        
        # check if day is in the list
        if day not in day_list:
            day_list.append(day)
            distribution.append({"day": day, "commit_count": trend["activity"], "frequency": 1})
        else:
            # get the index of the day
            index = day_list.index(day)
            # increment the commit count
            distribution[index]["commit_count"] += trend["activity"]
            distribution[index]["frequency"] += 1
    return distribution