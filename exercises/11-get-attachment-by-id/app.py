import requests

def get_attachment_by_id(attachment_id):
    # Your code here
    attachments_list = []
    response = requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')
    response_dict = response.json()
    for post in response_dict['posts']:
        attachments = post['attachments']
        if len(attachments) > 0 and attachments[0]['id'] == attachment_id:
            return attachments[0]['title']

print(get_attachment_by_id(137))