import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
time_dict = response.json()
hrs = time_dict['hours']
mins = time_dict['minutes']
sec = time_dict['seconds']
print(f'Current time: {hrs} hrs {mins} min and {sec} sec')