import csv
import json
import os

from analyzer.counter import count_lines
from utils import try_numeric


def generate_analysis_csv(csv_path):
    os.system(f'pmd -d ./repos/ -R rulesets/java/quickstart.xml,ruleset.xml -f csv > {csv_path}')


def generate_dictionary(csv_path):
    try:
        with open(csv_path) as f:
            a = [{k: try_numeric(v) for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
            return a
    except:
        return {}


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
    return 1 - (line_count['errorLines']/line_count['codeLines'])


def generate_report(csv_path):
    inspections = generate_dictionary(csv_path)
    line_count = count_lines('./repos', ['.java', '.js'])
    line_count['errorLines'] = len(inspections)
    performance_score = get_performance(line_count)
    with open('data.json', 'w') as outfile:
        json.dump(inspections, outfile, sort_keys=True, indent=4,
                  ensure_ascii=False)
    ruleset_count = 0
    categorized = categorize_inspections(inspections)
    for rulesetKey, rulesetVal in categorized.items():
        rule_count = 0
        ruleset_count += 1
        print(f'{ruleset_count}: {rulesetKey}')
        for ruleKey, ruleVal in rulesetVal.items():
            rule_count += 1
            print(f' > {rule_count}: {ruleKey} ({len(ruleVal)} issues)')
    print('=' * 20)
    print(f'Total code lines: {line_count["codeLines"]}')
    print(f'Total lines with violations: {line_count["errorLines"]}')
    print(f'Performance Score: {"{0:.2%}".format(performance_score)}')
    print('=' * 20)
