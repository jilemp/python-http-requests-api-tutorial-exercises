import requests

def get_post_tags(post_id):
    # Your code here
    tags = []
    response = requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')
    response_dict = response.json()
    for post in response_dict['posts']:
        if post['id'] == post_id:
            tags = post['tags']
    return tags


print(get_post_tags(146))