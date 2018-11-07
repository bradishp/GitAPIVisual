from github import Github

# Create Github instance
g = Github("XanthusXX", "password")

# Test get repositories:
for repo in g.get_user().get_repos():
    print(repo.name)

