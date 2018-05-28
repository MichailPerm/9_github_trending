import requests
from datetime import date, timedelta


API_REPO_URL = 'https://api.github.com/search/repositories'
API_ISSUES_URL = 'https://api.github.com/repos/{}/issues'


def get_trending_repositories(date_week_earlier):
    repo_quantity = 20
    request_params = {'q': 'created:<{}'.format(date_week_earlier)}
    repo_data_dict = requests.get(
        API_REPO_URL, params=request_params
    ).json()
    repo_list = repo_data_dict['items']
    return sorted(
        repo_list,
        key=lambda x: x['stargazers_count'],
        reverse=True
    )[:repo_quantity]


def get_open_issues_amount(repo_list_sorted):
    for repo in repo_list_sorted:
        issues = requests.get(
            API_ISSUES_URL.format(repo['full_name'])
        ).json()
        open_issues = [issue for issue in issues if issue['state'] == 'open']
        yield {'repo_name': repo['full_name'],
               'open_issues': open_issues}


if __name__ == '__main__':
    date_a_week_ago = date.today() - timedelta(days=7)
    trending_repo_list = get_trending_repositories(date_a_week_ago)
    open_issues_amount = get_open_issues_amount(trending_repo_list)
    for open_issues in open_issues_amount:
        print('For repo {} got next opened issues:'.format(
            open_issues['repo_name'])
        )
        for open_issue in open_issues['open_issues']:
            print('\t{}, url: {}'.format(
                open_issue['title'],
                open_issue['url'])
            )
