from backend import app
from flask import render_template, request, redirect, make_response
from flask_cors import cross_origin
from .__help__ import send_query, login_user, logout_user, get_user

'''
                    TEMPLATE            Страница входа.
    /login          login()             Вход пользователя.
    /logout         logout()            Выход пользователя.
'''


TEMPLATE = 'login.html'


@app.route("/login", methods=['GET', 'POST'])
@cross_origin()
def login():
    current_user = get_user(request)
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        try:
            user_login = request.form['login']
            user_password = request.form['psw']
        except Exception:
            return render_template(TEMPLATE, error='Некорректные данные')

        data = {'password': user_password, 'login': user_login}
        status, ans = send_query('login', data, 'post')
        if status == 200:
            resp = make_response(render_template(TEMPLATE))
            login_user(resp, ans)
            return resp
        else:
            return render_template(TEMPLATE, error='Пользователя с логином {0} и паролем {1} не существует'
                                   .format(user_login, user_password))
    return render_template(TEMPLATE)


@app.route("/logout")
@cross_origin()
def logout():
    resp = make_response(redirect('/'))
    logout_user(resp)
    return resp


@app.route("/registration", methods=['GET', 'POST'])
@cross_origin()
def sign_up():
    current_user = get_user(request)
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        try:
            user_login = request.form['login']
            name = request.form['name']
            email = request.form['email']
            password1 = request.form['psw1']
            password2 = request.form['psw2']
        except Exception:
            return render_template(TEMPLATE, error='Некорректные данные')
        if password1 != password2:
            return render_template(TEMPLATE, error='Ваши Пароли не совпадаю')
        data = {'password': password1, 'login': user_login, 'name': name, 'email': email}
        status, ans = send_query('reg', data, 'post')
        if ans['status'] == 'already':
            return render_template(TEMPLATE, error='Пользователь с таким логином или почтой уже существует')
        resp = make_response(render_template(TEMPLATE))
        login_user(resp, ans)
        return resp

    return render_template(TEMPLATE)
