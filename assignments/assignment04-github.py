from github import Github
from config import config as cfg

# Reading my API Key from the secure config file
apikey = cfg["githubkey"]

# Using the Github API module with the API key, hosting this connection in a variable called g
g = Github(apikey)

# using get_repo to connnect to the target, throught the secure connection in the variable g
repo = g.get_repo("DaveAero/aprivateone")

# getting the contents of the repo and saving them as a variable
contents =  repo.get_contents("text.txt")

# the contents needs to be decoded from markdown to see the text inside, https://github.com/PyGithub/PyGithub/issues/576
bytesData = (contents.decoded_content)

#this data is in bytes, converting to strings
RawData = bytesData.decode('UTF-8')

#print(RawData)

# Replacing the occurances of andrew. Could have used Regular expression here to find all matches regardless of Upper or Lower case 
stepOne = RawData.replace("andrew", "david")
newContents = stepOne.replace("Andrew", "David")

#print(newContents.encode('UTF-8'))

# Update README.md https://pygithub.readthedocs.io/en/stable/github_objects/Repository.html?highlight=update_file#github.Repository.Repository.update_file
repo.update_file("text.txt", "Changed Andrews to Davids", newContents.encode('UTF-8'), contents.sha)

g.close()
print("It got to here")