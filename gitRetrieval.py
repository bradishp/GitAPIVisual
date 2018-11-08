from github import Github
import sys
def get_info_on_developer(name=None, password=None):
    if name is None or password is None:
        g = Github("bbbbce0775c88233af65f275dadf6662e5531562") # Default Github instance using my token
    else:
        g= Github(name, password)

    print g.get_user().login + "'s repositories:"

    collaborators = set([])
    for repo in g.get_user().get_repos():
        print repo.name + ", ",
        for contributor in repo.get_contributors():
            if contributor.login != g.get_user().login:
                collaborators.add(contributor)

    print "\nThe public repositories of people who have worked with " + g.get_user().login + ":"
    for person in collaborators:
        print "\n" + person.login + ":",   
        for repo in person.get_repos():
            print repo.name + ", ",  
    sys.stdout.flush()
    return True
