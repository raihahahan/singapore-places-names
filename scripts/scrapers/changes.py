## Detects changes to the wikipedia page if any.
## Checks the 'Last updated' value against the previous value in wikiChanges.txt.
## If any change, then update this value on wikiChanges.txt and push this value to github.
## Run this script every day with Crontab.

from mainWikiScrape import getWikiData
import sys
import base64
from github import Github
from github import InputGitTreeElement
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv() 

def pushToGithubMain(file_names: list[str], commit_message: str):
    try:
        # credits: with help from https://stackoverflow.com/a/50072113
        config = dotenv_values(".env")
        user = config["user"]
        password = config["githubPK"]
        file_list = [config["fileLocation"]]
        repo = "singapore-places-names"
        g = Github(user,password)
        
        repo = g.get_user().get_repo(repo) # repo name
        main_ref = repo.get_git_ref('heads/main')
        main_sha = main_ref.object.sha
        base_tree = repo.get_git_tree(main_sha)

        element_list = list()
        for i, entry in enumerate(file_list):
            with open(entry) as input_file:
                data = input_file.read()
            if entry.endswith('.png'): # images must be encoded
                data = base64.b64encode(data)
            element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
            element_list.append(element)

        tree = repo.create_git_tree(element_list, base_tree)
        parent = repo.get_git_commit(main_sha)
        commit = repo.create_git_commit(commit_message, tree, [parent])
        main_ref.edit(commit.sha)
    except:
        print(sys.exc_info()[0])

def updateTxtFile(file: str, newVal: str):
    try:
        with open(file, "w") as g:
                g.write(newVal)
                print("Text file updated successfully.")
    except:
        print(sys.exc_info()[0])


def detectChange():
    file_name = "wikiChanges.txt"
    commit_msg = "Updated wikiChanges.txt with Python bot."

    try:  
        soup = getWikiData()
        lastmod = soup.find("li", { "id": "footer-info-lastmod"}).get_text().strip()
        lastUpd = ""
        with open(file_name) as f:
            lastUpd = f.readline()
        if (lastUpd == lastmod):
            print("No changes detected.")
        else:
            print("A change is found:\n\nPrevious update: " + lastUpd + "\nMost recent update: " + lastmod)
            updateTxtFile(file_name, lastmod)

            try:
                pushToGithubMain([file_name], commit_msg)  
            except:
                print(sys.exc_info()[0])        
            
    except:
        print(sys.exc_info()[0])
        return 

detectChange()