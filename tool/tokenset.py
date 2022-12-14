from itsdangerous import URLSafeSerializer as safter
from flask import g
from create_table import password
from tool.redis import redis_db
import config
import base64
from tool.resp import response


class OperateToken:
    def __init__(self):
        self._private_key = config.security_key
        self.salt = base64.encodebytes(self._private_key.encode('utf8'))

    def create_token(self, user_name):
        object_ = safter(self._private_key)
        return object_.dumps({
            "username": user_name
        }, self.salt)

    def decode_token(self, token):
        object_ = safter(self._private_key)
        return object_.loads(token, salt=self.salt)

    def validate_token(self, token_):
        data = {'code': 40101}
        print(token_)
        try:
            info = self.decode_token(token_)
        except:
            return response(data=data, msg="非法授权", status=401)
        print(info)
        user_ = password.query.filter(password.username == info["username"]).first()
        print(user_)
        if not user_:
            return response(data=data, msg="当前用户不存在", status=401)
        else:
            if not redis_db.get(token_):
                return response(data=data, msg="用户授权已过期", status=401)
            g.user = {
                "id": user_
            }
        return None


operate_token = OperateToken()
