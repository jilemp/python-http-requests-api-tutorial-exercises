import requests

def get_titles():
    # Your code here
    titles = []
    response = requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')
    response_dict = response.json()
    for post in response_dict['posts']:
        title = post['title']
        titles.append(title)
    return titles


print(get_titles())