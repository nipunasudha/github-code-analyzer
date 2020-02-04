from utils import query_yes_no
from utils.utils import get_repo_list, delete_dir, clone_by_url

while True:
    username = input('Enter username to fetch repositories: ')
    # username = 'upulrangana'  # todo remove this
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
        delete_dir('./repos')
        if proceed:
            for url in repo_list:
                clone_by_url(url)
        else:
            print('User aborted analysis.')
        break
