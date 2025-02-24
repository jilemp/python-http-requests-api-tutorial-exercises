import requests

url = "https://assets.breatheco.de/apis/fake/sample/save-project-json.php"

my_obj = {
    "id": 2323,
    "title": "Very big project"
    }

headers = {'Content-Type': 'application/json'}

response = requests.post(url, json = my_obj, headers=headers)

print(response.text)