import requests


def send_query(url, data={}, method='GET'):
    url = 'http://192.168.88.111:5000/' + url
    method = method.upper()
    if method == 'GET':
        r = requests.get(url, json=data)
    elif method == 'POST':
        r = requests.post(url, json=data)
    return r.status_code, r.json()
