import csv
import json
import os

from analyzer.counter import count_lines
from analyzer.repo_info import RepoInfoFetcher
from utils import try_numeric

DATA_JSON_PATH = './outputs/data.json'
META_JSON_PATH = './outputs/meta.json'


def generate_analysis_csv(csv_path):
    os.system(f'pmd -d ./repos/ -R rulesets/java/quickstart.xml,ruleset.xml -f csv > {csv_path}')


def generate_dictionary(csv_path):
    try:
        with open(csv_path) as f:
            a = [{k: try_numeric(v) for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
            return a
    except:
        return {}


def generate_meta_json(username):
    repo_meta = RepoInfoFetcher.get_repo_info(username)
    with open(META_JSON_PATH, 'w') as outfile:
        json.dump(repo_meta, outfile, sort_keys=True, indent=4,
                  ensure_ascii=False)


def categorize_inspections(unsorted_inspections):
    inspections = {}
    for item in unsorted_inspections:
        ruleset = item['Rule set']
        rule = item['Rule']
        if ruleset not in inspections:
            inspections[ruleset] = {}
        if rule not in inspections[ruleset]:
            inspections[ruleset][rule] = []
        inspections[ruleset][rule].append(item)
    return inspections


def get_performance(line_count):
    return 1 - (line_count['errorLines'] / line_count['codeLines'])


def get_formatted_meta():
    import json
    meta_raw = open(META_JSON_PATH).read()
    meta = json.loads(meta_raw)
    meta_str = ''
    meta_str += f'Total repositories: {meta["repo_count"]}\n'
    meta_str += f'Total commits: {meta["total_commits"]}\n'
    languages = meta["languages"]
    meta_str += f'{len(languages)} Languages\n'
    for lang, chars in languages.items():
        meta_str += f'({lang}: {chars} bytes )'
    return meta_str + '\n'


def generate_report(csv_path):
    report = ''
    inspections = generate_dictionary(csv_path)
    line_count = count_lines('./repos', ['.java', '.js'])
    line_count['errorLines'] = len(inspections)
    performance_score = get_performance(line_count)
    with open(DATA_JSON_PATH, 'w') as outfile:
        json.dump(inspections, outfile, sort_keys=True, indent=4,
                  ensure_ascii=False)
    ruleset_count = 0
    categorized = categorize_inspections(inspections)
    for rulesetKey, rulesetVal in categorized.items():
        rule_count = 0
        ruleset_count += 1
        report += f'{ruleset_count}: {rulesetKey}\n'
        for ruleKey, ruleVal in rulesetVal.items():
            rule_count += 1
            report += f' > {rule_count}: {ruleKey} ({len(ruleVal)} issues)\n'
    report += '=' * 20 + '\n'
    report += get_formatted_meta()
    report += f'Total code lines: {line_count["codeLines"]}\n'
    report += f'Total lines with violations: {line_count["errorLines"]}\n'
    report += f'Performance Score: {"{0:.2%}".format(performance_score)}\n'
    report += '=' * 20 + '\n'
    return report
