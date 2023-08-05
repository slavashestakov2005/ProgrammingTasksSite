import json
import requests


server = 'http://192.168.89.246:5000/'
cookie_fields = ['jwt_access', 'jwt_refresh', 'current_user']


def send_simple_query(url, data=None, method='GET', headers=None):
    if data is None:
        data = {}
    if headers is None:
        headers = []
    url = server + url
    method = method.upper()
    if method == 'GET':
        r = requests.get(url, json=data, headers=headers)
    elif method == 'POST':
        r = requests.post(url, json=data, headers=headers)
    print(r.status_code)
    print(r.content)
    return r.status_code, r.json()


def send_query(url, jwt_refresh, data=None, method='GET'):
    refresh_head = {"Authorization": "Bearer {}".format(jwt_refresh)}
    jwt_access = requests.get(server + "refresh", headers=refresh_head).json()["jwt_access"]
    access_head = {"Authorization": f"Bearer {jwt_access}"}
    return send_simple_query(url, data, method, access_head)


def login_user(response, ans):
    response.set_cookie('jwt_access', ans['jwt_access'])
    response.set_cookie('jwt_refresh', ans['jwt_refresh'])
    response.set_cookie('current_user', json.dumps(ans['user']))


class User:
    def __init__(self, auth, data):
        self.is_authenticated = auth
        self.access, self.refresh, self.info = data
        self.info = json.loads(self.info)


def get_user(request) -> User:
    if all(cookie in request.cookies for cookie in cookie_fields):
        return User(True, [request.cookies[cookie] for cookie in cookie_fields])
    return User(False, ['', '', json.dumps({})])


def logout_user(response):
    for cookie in cookie_fields:
        response.delete_cookie(cookie)
