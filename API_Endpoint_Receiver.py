import requests
import json

# r = requests.post(
#     'https://collect2.com/api/f1201a0c-c7cd-4ec5-8605-a95ff1cd274d/datarecord/',
#     json={"action": "opened", "issue": {"name": "Hello", "number": 1347},
#           "repository": {"id": 1296269, "full_name": "octocat/Hello-World", "owner": {"login": "octocat", "id": 1}}})




# r = requests.get('https://collect2.com/api/f1201a0c-c7cd-4ec5-8605-a95ff1cd274d/datarecord/')
#
#
# print(r.json()
#       )

r = {'count': 1, 'next': None, 'previous': None, 'results': [{'datetime': '2021-02-11T12:15:03.150088Z', 'dataset': 'etsy_callback', 'record': {'expires_in': 3600, 'token_type': 'Bearer', 'access_token': '12345678.O1zLuwveeKjpIqCQFfmR-PaMMpBmagH6DljRAkK9qt05OtRKiANJOyZlMx3WQ_o2FdComQGuoiAWy3dxyGI4Ke_76PR', 'refresh_token': '12345678.JNGIJtvLmwfDMhlYoOJl8aLR1BWottyHC6yhNcET-eC7RogSR5e1GTIXGrgrelWZalvh3YvvyLfKYYqvymd-u37Sjtx'}, 'id': 1125092, 'meta_data': {'ip': '81.174.143.188', 'headers': {'Host': 'collect2.com', 'Accept': 'application/json', 'Origin': 'https://collect2.com', 'Referer': 'https://collect2.com/data-set/etsy_callback/', 'Connection': 'close', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15', 'X-Csrftoken': 'XuhRxUFNSQsl5OVq0NoMghOyOPAVf0zZIdIPA9a139ps9gp8h6vnOCcZtm8WRok4', 'Content-Type': 'application/json', 'Content-Length': '278', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-gb', 'X-Requested-With': 'XMLHttpRequest'}}}]}

def extract_element_from_json(obj, path):
    '''
    Extracts an element from a nested dictionary or
    a list of nested dictionaries along a specified path.
    If the input is a dictionary, a list is returned.
    If the input is a list of dictionary, a list of lists is returned.
    obj - list or dict - input dictionary or list of dictionaries
    path - list - list of strings that form the path to the desired element
    '''
    def extract(obj, path, ind, arr):
        '''
            Extracts an element from a nested dictionary
            along a specified path and returns a list.
            obj - dict - input dictionary
            path - list - list of strings that form the JSON path
            ind - int - starting index
            arr - list - output list
        '''
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr
    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr


record = extract_element_from_json(r, ["results", 'record'])
access_token = extract_element_from_json(record, ['access_token'])

refresh_token = extract_element_from_json(record, ['refresh_token'])

print('access_token 'f'{access_token}')
print('refresh_token 'f'{refresh_token}')

