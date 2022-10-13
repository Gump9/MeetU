from util import db
import tool.tokenset as tk
from create_table import password
from tool.redis import redis_db
import tool.config_redis as cr
from tool.resp import response


def user_login(username, passw):
    token = None
    user1 = password.query.filter(password.username == username).first()
    if not user1:
        return response(data={"code": 40101}, msg="该用户不存在,请创建用户", status=401)

    elif (user1.password == passw):
        token = tk.operate_token.create_token(username)
        redis_db.set(token, token, cr.expire_time)
        return token
    else:
        return response(data={"code": 40101}, msg="密码错误", status=401)
