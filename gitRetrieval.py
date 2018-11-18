import sys
from github import Github
import json

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

def generate_info(username):
    github_instance = Github()
    user = github_instance.get_user(username)
    languages_in_repos = get_languages_in_repositories(user)
    total_languages = calculate_language_total(languages_in_repos)
    print total_languages
    json_string = json.dumps(total_languages)
    print json_string
    return json_string

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else: 
        username = "XanthusXX"  # Default value
    generate_info(username)