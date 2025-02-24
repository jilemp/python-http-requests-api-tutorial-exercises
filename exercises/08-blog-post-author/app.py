import requests

# Your code here
response = requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')
response_dict = response.json()
print(response_dict['posts'][0]['author']['name'])
