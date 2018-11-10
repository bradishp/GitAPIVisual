import sys
from github import Github

class GitUserInfo:

    def __init__(self, user_identifier, password=None):
        if password is None:
            self.github_instance = Github(user_identifier)
        else:
            self.github_instance = Github(user_identifier, password)

    def display_developer_repos(self):
        repo_list = self.github_instance.get_user().login + "'s repositories: "

        for repo in self.github_instance.get_user().get_repos():
            repo_list += repo.name + ", "
        print repo_list[:-2]
        sys.stdout.flush()
        return True

    def gather_info_on_collaborators(self):
        collaborators_repos = "The public repositories of people who have worked with " + self.github_instance.get_user().login + ": \n"
        collaborators = set([])
        for repo in self.github_instance.get_user().get_repos():
            for contributor in repo.get_contributors():
                if contributor.login != self.github_instance.get_user().login:
                    collaborators.add(contributor)
        for person in collaborators:
            collaborators_repos += person.login + ": "  
            for repo in person.get_repos():
                collaborators_repos += repo.name +  ", "
            collaborators_repos += "\n"
        print collaborators_repos
        sys.stdout.flush()
        return True


