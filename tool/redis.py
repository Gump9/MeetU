import redis


class RedisDB():
    def __init__(self):
        redis_pool = redis.ConnectionPool(host="127.0.0.1", port=6379)  # 默认端口号
        self.__strict_redis = redis.StrictRedis(connection_pool=redis_pool)

    def set(self, key, value, expiry):
        self.__strict_redis.set(name=key, value=value, ex=expiry)

    def get(self, key):
        return self.__strict_redis.get(key)

    def ttl(self, key):
        return self.__strict_redis.ttl(key)


redis_db = RedisDB()
