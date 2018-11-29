import sys
from github import Github
import json

minor_languages = {}

def get_languages_in_repositories(github_user):
    languages_in_repositories = []
    for repo in github_user.get_repos():
        dict = repo.get_languages()
        languages_in_repositories.append(dict)
    return languages_in_repositories

def calculate_language_total(list):
    totalLinesByLanguage = {}
    totalLines = 0
    for dict in list:
        for key in dict.keys():
            if totalLinesByLanguage.has_key(key): 
                totalLinesByLanguage[key] += dict.get(key)
            else:
                totalLinesByLanguage[key] = dict.get(key)
            totalLines += dict.get(key)
    return filter_languages(totalLinesByLanguage, totalLines)

def filter_languages(totalLinesByLanguage, totalLines):
    global minor_languages
    filtered_languages = {}
    for key in totalLinesByLanguage.keys():
        percentage = ((totalLinesByLanguage[key] / float(totalLines)) * 100)
        if (percentage) < 1.5:
            minor_languages[key] = totalLinesByLanguage[key]
            if filtered_languages.has_key("Other"):
                filtered_languages["Other"] += totalLinesByLanguage[key]
            else:
                filtered_languages["Other"] = totalLinesByLanguage[key]
        else:
            filtered_languages[key] = totalLinesByLanguage[key]
    return filtered_languages

def convert_to_json(total_languages):
    json_languages = []
    for key in total_languages.keys():
        json_element = {}
        json_element["language"] = key
        json_element["linesOfCode"] = total_languages[key]
        json_languages.append(json_element)
    json_string = json.dumps(json_languages)
    return json_string

def generate_info(username):
    github_instance = Github('bbbbce0775c88233af65f275dadf6662e5531562')
    user = github_instance.get_user(username)
    languages_in_repos = get_languages_in_repositories(user)
    total_languages = calculate_language_total(languages_in_repos)
    return convert_to_json(total_languages)

def get_minor_languages():
    global minor_languages
    return convert_to_json(minor_languages)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else: 
        username = "XanthusXX"  # Default value
    generate_info(username)