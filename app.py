from flask import Flask, request, g, redirect, url_for
import config
from tool.login import user_login
from util import db
from create_table import user, password
from tool.tokenset import operate_token
from tool.resp import response

app = Flask(__name__)
ctx = app.app_context()
ctx.push()
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db.init_app(app)
# app.config.from_object(config)
db.create_all()


@app.before_request
def before_request():
    if request.path not in config.NOT_CHECK_URL:
        try:
            token_ = request.headers['token']
        except:
            return response(data={'code': 40101}, msg="无访问权限", status=401)
        res = operate_token.validate_token(token_)
        return res
    else:
        token_ = request.headers['token']
        res = None
    if res:
        return res


@app.route('/register')
def register():
    password1 = password(username="wht", password="123456")
    db.session.add(password1)
    db.session.commit()
    return response(data={"code": 40101}, msg="注册成功", status=200)


@app.route('/insert')
def insert():
    user1 = user(username="wht", school="seu")
    db.session.add(user1)
    db.session.commit()
    return response(data={"code": 40101}, msg="插入成功", status=200)


@app.route('/login')
def login():
    return user_login("wht", "123456")


@app.route('/')
def hello_world():
    return redirect("/login")


if __name__ == '__main__':
    app.run()
