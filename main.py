from utils import query_yes_no
from utils.utils import get_repo_list, generate_scan_csv, clone_by_url, empty_dir


def execute_command(cmd):
    if cmd == 'clone':
        username = input('Enter username to fetch repositories: ')
        if username.strip() is '':
            print('Invalid username! Please try again.')
            return
        else:
            repo_list = get_repo_list(username)
            repo_count = len(repo_list)
            if repo_count == 0:
                print(f'No repositories found for user \'{username}\'! Please try again.')
                return
            proceed = query_yes_no(
                f'Do you want to clone all {repo_count} repositories found for the user \'{username}\'?')
            empty_dir('./repos')
            if proceed:
                for url in repo_list:
                    clone_by_url(url)
            else:
                print('User aborted cloning.')
    elif cmd == 'scan':
        csv_path = generate_scan_csv()
        # fields = ['Problem', 'Package', 'File', 'Priority', 'Line', 'Description', 'Rule set', 'Rule']
        # results = parse_csv_by_field(csv_path, ['Problem', 'Rule'])
        # print(results)
    elif cmd == 'exit':
        exit()
    elif cmd == 'help':
        print('clone - Clone all repositories from a user\n'
              'scan - Scan cloned repositories and generate report\n'
              'help - Get this command guid\n'
              'exit - Exit application')
    else:
        print('Invalid command!')


while True:
    command = input("Enter command to execute ('help' to learn about commands) >>")
    execute_command(command)
# execute_command('scan')
