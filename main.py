import os

from utils import query_yes_no
from utils.utils import get_repo_list, clone_by_url, empty_dir

while True:
    # username = input('Enter username to fetch repositories: ')
    username = 'githubanalyzeruser'  # todo remove this
    if username.strip() is '':
        print('Invalid username! Please try again.')
        continue
    else:
        repo_list = get_repo_list(username)
        repo_count = len(repo_list)
        if repo_count == 0:
            print(f'No repositories found for user \'{username}\'! Please try again.')
            continue
        proceed = query_yes_no(f'Do you want to clone all {repo_count} repositories found for the user \'{username}\'?')
        empty_dir('./repos')
        if proceed:
            for url in repo_list:
                clone_by_url(url)
        else:
            print('User aborted analysis.')
        break

os.system('pmd -d ./repos/ -R rulesets/java/quickstart.xml,ruleset.xml -f html > output.html')