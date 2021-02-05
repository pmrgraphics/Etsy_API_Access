import requests

# r = requests.post(
#     'https://collect2.com/api/f1201a0c-c7cd-4ec5-8605-a95ff1cd274d/datarecord/',
#     json={"action": "opened", "issue": {"name": "Hello", "number": 1347},
#           "repository": {"id": 1296269, "full_name": "octocat/Hello-World", "owner": {"login": "octocat", "id": 1}}})




r = requests.get('https://collect2.com/api/f1201a0c-c7cd-4ec5-8605-a95ff1cd274d/datarecord/')
print(r.text)