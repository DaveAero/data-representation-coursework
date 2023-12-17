from github import Github
from config import config as cfg

filename = "test.txt"

apikey = cfg["githubkey"]
# use your own key

g = Github(apikey)

repo = g.get_repo("DaveAero/aprivateone")
print(repo.clone_url)

#for repo in g.get_user().get_repos():
#    print(repo.name)

with open(filename, "w") as f:
        # write takes a string so we need to convert
        f.write(repo.clone_url)