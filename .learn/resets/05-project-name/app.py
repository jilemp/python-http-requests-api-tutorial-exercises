import requests

# Your code here
response = requests.get('https://assets.breatheco.de/apis/fake/sample/project1.php')

if response.status_code == 200:
    response_dict = response.json()
    name = response_dict['name']
    print(name)
else:
    print("Data extraction failed")