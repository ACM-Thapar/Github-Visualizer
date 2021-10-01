import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
# get data from github profile

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