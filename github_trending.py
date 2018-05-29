import requests
from datetime import date, timedelta


def get_trending_repositories(date_week_earlier):
    API_REPO_URL = 'https://api.github.com/search/repositories'
    repo_quantity = 20
    request_params = {'q': 'created:<{}'.format(date_week_earlier), 's': 'stars'}
    repo_data_dict = requests.get(
        API_REPO_URL, params=request_params
    ).json()
    repo_list = repo_data_dict['items']
    return repo_list[:repo_quantity]


def get_open_issues(repo):
    API_ISSUES_URL = 'https://api.github.com/repos/{}/issues'
    issues = requests.get(
        API_ISSUES_URL.format(repo['full_name'])
    ).json()
    open_issues = [issue for issue in issues if issue['state'] == 'open']
    return open_issues


if __name__ == '__main__':
    date_a_week_ago = date.today() - timedelta(days=7)
    trending_repo_list = get_trending_repositories(date_a_week_ago)
    for repo in trending_repo_list:
        open_issues = get_open_issues(repo)
        print('For repo {} got next opened issues:'.format(
            repo['full_name']
        ))
        for issue in open_issues:
            print('\t{}, url: {}'.format(
                issue['title'],
                issue['url'])
            )
