import requests


def send_query(url, data={}, method='GET'):
    url = 'http://192.168.88.111:5000/' + url
    method = method.upper()
    if method == 'GET':
        r = requests.get(url, json=data)
    elif method == 'POST':
        r = requests.post(url, json=data)
    return r.status_code, r.json()


cookie_fields = ['jwt_access', 'jwt_refresh', 'current_user']


def login_user(response, ans):
    response.set_cookie('jwt_access', ans['jwt_access'])
    response.set_cookie('jwt_refresh', ans['jwt_refresh'])
    response.set_cookie('current_user', str(ans['user']))


class User:
    def __init__(self, auth, data):
        self.is_authenticated = auth
        self.access, self.refresh, self.info = data


def get_user(request) -> User:
    if all(cookie in request.cookies for cookie in cookie_fields):
        return User(True, [request.cookies[cookie] for cookie in cookie_fields])
    return User(False, ['', '', ''])


def logout_user(response):
    for cookie in cookie_fields:
        response.delete_cookie(cookie)
