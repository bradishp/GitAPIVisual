import sys
from github import Github
import json


class GitLanguagesRetrieval:

    def __init__(self, username, tokken = ""):
        self.username = username
        self.minor_languages = {}
        self.language_appearences = {}
        self.language_collaborators = {}
        github_instance = None
        if tokken == "":
            github_instance = Github()
        else:
            github_instance = Github(tokken)
        user = github_instance.get_user(username)
        languages_in_repos = self.get_languages_in_repositories(user)
        self.main_languages = self.calculate_language_total(languages_in_repos)


    def get_languages_in_repositories(self, github_user):
        languages_in_repositories = []
        for repo in github_user.get_repos():
            contributors = 0
            for _ in repo.get_contributors():
                contributors+=1
            dict = repo.get_languages()
            dict["contributors"] = contributors
            languages_in_repositories.append(dict)
        return languages_in_repositories

    def calculate_language_total(self, list):
        totalLinesByLanguage = {}
        totalLines = 0
        for dict in list:
            contributors = dict["contributors"]
            del dict['contributors']
            for key in dict.keys():
                if totalLinesByLanguage.has_key(key):
                    totalLinesByLanguage[key] += dict.get(key)
                    self.language_appearences[key] += 1
                else:
                    totalLinesByLanguage[key] = dict.get(key)
                    self.language_appearences[key] = 1
                if self.language_collaborators.has_key(key):
                    self.language_collaborators[key] += contributors
                else:
                    self.language_collaborators[key] = contributors
                totalLines += dict.get(key)
        return self.filter_languages(totalLinesByLanguage, totalLines)

    def filter_languages(self, totalLinesByLanguage, totalLines):
        filtered_languages = {}
        for key in totalLinesByLanguage.keys():
            percentage = ((totalLinesByLanguage[key] / float(totalLines)) * 100)
            if (percentage) < 1.5:
                self.minor_languages[key] = totalLinesByLanguage[key]
                if filtered_languages.has_key("Other"):
                    filtered_languages["Other"] += totalLinesByLanguage[key]
                else:
                   filtered_languages["Other"] = totalLinesByLanguage[key]
            else:
                filtered_languages[key] = totalLinesByLanguage[key]
        return filtered_languages

    def convert_to_json(self, total_languages, valueName):
        json_languages = []
        for key in total_languages.keys():
            json_element = {}
            json_element["language"] = key
            json_element[valueName] = total_languages[key]
            json_languages.append(json_element)
            json_string = json.dumps(json_languages)
        return json_string

    def get_main_languages(self):
        return self.convert_to_json(self.main_languages, "linesOfCode")

    def get_minor_languages(self):
        return self.convert_to_json(self.minor_languages, "linesOfCode")

    def get_languages_appearences(self):
        major_appearences = {}
        for language in self.main_languages.keys():
            if self.language_appearences.has_key(language):
                major_appearences[language] = self.language_appearences[language]
        return self.convert_to_json(major_appearences, "numberOfRepos")

    def get_average_collaborators(self):
        average_collaborators = {}
        for language in self.main_languages.keys():
            if self.language_appearences.has_key(language):
                print self.language_collaborators[language]
                print self.language_appearences[language]
                average_collaborators[language] = (self.language_collaborators[language] / float(self.language_appearences[language]))
        return self.convert_to_json(average_collaborators, "numberOfRepos")

    def get_username(self):
        return json.dumps(self.username)

if __name__ == "__main__":
    username = "mbostock"   # Default values
    tokken = ""
    if len(sys.argv) > 1:   # Can specify from the command line
        username = sys.argv[1]
    if len(sys.argv) > 2:
        tokken = sys.argv[2]  
    users_language_info = GitLanguagesRetrieval(username, tokken) 
    print users_language_info.get_main_languages()