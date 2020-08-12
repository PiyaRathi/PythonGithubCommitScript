from github import Github
import os
from pprint import pprint
from github import InputGitTreeElement

token = os.getenv('GITHUB_TOKEN', 'f753eb7a2b07d0723e5311c0b814d5fdb8e1f2f4')
g = Github(token)

repo = g.get_repo("PiyaRathi/myApp")
print(repo)

master_ref = repo.get_git_ref('heads/master')

print(master_ref)

file_list = [
    'CrudDemo.py',
    'Hello.py'
]
master_sha = master_ref.object.sha

print(master_sha)
base_tree = repo.get_git_tree(master_sha)
element_list = list()
for entry in file_list:
    with open(entry, 'r') as input_file:
        data = input_file.read()
    element = InputGitTreeElement(entry, '100644', 'blob', data)
    element_list.append(element)
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit("Test commit", tree, [parent])
master_ref.edit(commit.sha)


print("--File pushed to git repo--")
