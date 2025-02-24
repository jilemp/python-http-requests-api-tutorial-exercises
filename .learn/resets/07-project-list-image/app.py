import requests

# Your code here
response = requests.get('https://assets.breatheco.de/apis/fake/sample/project_list.php')
response_dict = response.json()
print(response_dict[-1]['images'][-1])