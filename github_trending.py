import requests


from datetime import date, timedelta


API_REPO_URL = 'https://api.github.com/search/repositories?q=created:>{}'


def get_trending_repositories(top_size):
    pass


def get_open_issues_amount(repo_owner, repo_name):
    pass

if __name__ == '__main__':
    days_in_week = 7
    week_ago = date.today() - timedelta(days=days_in_week)
    search_url = API_REPO_URL.format(week_ago)
    repo_data = requests.get(search_url).json()
    print(repo_data)
