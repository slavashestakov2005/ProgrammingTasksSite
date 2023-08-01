from backend import app, login
from flask import render_template, request, redirect
from flask_cors import cross_origin
from flask_login import login_user, logout_user, current_user
from .__help__ import send_query

'''
                    TEMPLATE            Страница входа.
    /login          login()             Вход пользователя.
    /logout         logout()            Выход пользователя.
'''


TEMPLATE = 'login.html'


@login.user_loader
def load_user(id):
    return User.select(int(id))


@app.route("/login", methods=['GET', 'POST'])
@cross_origin()
def login():
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
            login_user(u)
            return redirect('/')
        else:
            return render_template(TEMPLATE, error='Пользователя с логином {0} и паролем {1} не существует'
                                   .format(user_login, user_password))
    return render_template(TEMPLATE)


@app.route("/logout")
@cross_origin()
def logout():
    logout_user()
    return redirect('/')


@app.route("/sign_up")
@cross_origin()
def sign_up():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'Input':
        if user_login == request.form['login']:
            return render_template(TEMPLATE, error='Логин уже занят, выберете другой')
        if password1 != password2:
            return render_template(TEMPLATE, error='Ваши Пароли не совпадаю')



        u = User.select_by_login(user_login)
        if u is not None and u.check_password(user_password):
            login_user(u)
            return redirect('/')
        else:
            return render_template(TEMPLATE, error='Пользователя с логином {0} и паролем {1} не существует'
                                   .format(user_login, user_password))
    return render_template(TEMPLATE)
