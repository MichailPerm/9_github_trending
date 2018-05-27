import requests
from datetime import date, timedelta


API_REPO_URL = 'https://api.github.com/search/repositories?q=created:<{}'
API_ISSUES_URL = 'https://api.github.com/repos/{}/issues'


def get_trending_repositories(date_week_earlier):
    repo_quantity = 20
    repo_data = requests.get(API_REPO_URL.format(date_week_earlier)).json()
    repo_list = repo_data['items']
    repo_list_sorted = sorted(repo_list, key=lambda x: x['stargazers_count'], reverse=True)[:repo_quantity]
    return repo_list_sorted


def get_open_issues_amount(repo_list_sorted):
    for repo in repo_list_sorted:
        repo_name = repo['full_name']
        issues = requests.get(API_ISSUES_URL.format(repo_name)).json()
        open_issues = [issue for issue in issues if issue['state'] == 'open']
        yield {'repo_name': repo_name,
               'open_issues': open_issues}

if __name__ == '__main__':
    date_week_earlier = date.today() - timedelta(days=7)
    repo_list_sorted = get_trending_repositories(date_week_earlier)
    issues_info = get_open_issues_amount(repo_list_sorted)
    for issues in issues_info:
        print('For repo {} got next opened issues:'.format(issues['repo_name']))
        for open_issue in issues['open_issues']:
            print('\t{}, url: {}'.format(open_issue['title'], open_issue['url']))
