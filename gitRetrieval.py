import sys
from github import Github
from app import app, set_display_info

def get_languages_in_repositories(github_user):
    languages_in_repositories = []
    for repo in github_user.get_repos():
        dict = repo.get_languages()
        languages_in_repositories.append(dict)
    return languages_in_repositories

def calculate_language_total(list):
        totalLinesByLanguage = {}
        for dict in list:
            for key in dict.keys():
                if totalLinesByLanguage.has_key(key): 
                    totalLinesByLanguage[key] += dict.get(key)
                else:
                    totalLinesByLanguage[key] = dict.get(key)
        return totalLinesByLanguage


if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else: 
        username = "XanthusXX"  # Default value
    github_instance = Github()
    user = github_instance.get_user(username)
    list = get_languages_in_repositories(user)
    print calculate_language_total(list)
    #app.run(host='0.0.0.0',port=5000,debug=True)