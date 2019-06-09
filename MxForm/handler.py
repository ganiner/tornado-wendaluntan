# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2019-06-09
#@Email : agamgn@163.com
import redis
from tornado.web import RequestHandler


class RedisHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.redis_conn = redis.StrictRedis(**self.settings["redis"])