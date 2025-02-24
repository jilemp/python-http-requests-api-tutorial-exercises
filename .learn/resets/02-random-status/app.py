import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")

status = response.status_code

if status == 404:
    print("The URL you asked for is not found")
elif status == 503:
    print("Unavailable right now")
elif status == 200:
    print("Everything went perfect")
elif status == 400:
    print("Something is wrong with the request params")
else:
    print("Unknown status code")