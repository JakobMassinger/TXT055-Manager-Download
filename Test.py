import requests
from github import Github

g=Github()
user=g.get_user("JakobMassinger")

def getCommits_url():    
    for repo in user.get_repos():
        print(repo)
        if repo.full_name=="JakobMassinger/TXT055-Manager-Download":
            return repo.get_commits()
c=getCommits_url()
print(c.__elements)
