from urllib.request import urlopen
import json
import subprocess, shlex

hostname = input("Enter hostname: ") 
groupId = input("Enter group id: ")
userId = input("Enter user id: ")
token = input("Enter access token: ")

allGroups     = urlopen("https://" + hostname + "/api/v4/groups/" + groupId + "?private_token=" + token + "&per_page=100000")
allGroupsDict = json.loads(allGroups.read().decode())
for project in allGroupsDict["projects"]:
    try:
        projectUrl  = project['http_url_to_repo'].replace("https://", "https://" + userId + ":" + token + "@")
        command     = shlex.split('git clone %s' % projectUrl)
        resultCode  = subprocess.Popen(command)

    except Exception as e:
        print("Error on %s: %s" % (projectUrl, e.strerror))

