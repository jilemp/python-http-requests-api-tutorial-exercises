import requests

# Your code here
url = 'https://assets.breatheco.de/apis/fake/sample/post.php'
my_obj = {'somekey': 'somevalue'}

x = requests.post(url, json = my_obj)

print(x.text)