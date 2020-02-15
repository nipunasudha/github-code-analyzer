from analyzer.analyzer_utils import generate_analysis_csv, generate_report
from utils import get_repo_list, empty_dir, clone_by_url


class Analyzer(object):
    def __init__(self):
        self.CSV_PATH = '../outputs/output.csv'

    @staticmethod
    def clone(printer, indicator, prompter, username):
        printer(f'Fetching repositories of user \'{username}\'...')
        indicator(f'Cloning from {username}...')

        if username.strip() is '':
            printer('Invalid username! Please try again.')
            indicator(f'Cloning failed.')
            return 1
        else:
            repo_list = get_repo_list(username)
            repo_count = len(repo_list)
            if repo_count == 0:
                printer(f'No repositories found for user \'{username}\'! Please try again.')
                indicator(f'Cloning failed.')
                return 2
            printer(f'Found {repo_count} repositories.')
            proceed = prompter(
                f'Do you want to clone all {repo_count} repositories found for the user \'{username}\'?')
            empty_dir('./repos')
            if proceed:
                for url in repo_list:
                    printer(f'Cloning repository \'{url}\'')
                    clone_by_url(url)
                printer(f'Cloned {repo_count} repositories successfully!')
                indicator(f'Cloning successful!')
                return 0
            else:
                printer('Cloning aborted by user. Previously cloned repositories might be removed!')
                indicator(f'Cloning aborted.')
                return -1

    def analyze(self, printer, indicator):
        printer('Analysis started.')
        try:
            generate_analysis_csv(self.CSV_PATH)
        except Exception as e:
            printer(f'Analysis failed!\n\nError Occured: {e}')
            return 1

        printer('Analysis completed. Click \'Report\' for a report.')
        return 0

    def report(self, printer, indicator):
        printer('============ REPORT START ============')
        generate_report(self.CSV_PATH)
        printer('============= REPORT END =============')
